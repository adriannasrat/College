create table customer (
custid number(10) not null,
username varchar2(30) not null,
password varchar2(40) not null
);
alter table customer add (
constraint customer_pk primary key (custid)
);
alter table customer add (
constraint customer_uk unique (username)
);

create sequence customer_seq;

CREATE OR REPLACE FUNCTION get_hash(
  p_username IN VARCHAR2,
  p_password IN VARCHAR2
) RETURN VARCHAR2
AS
  l_salt  CONSTANT VARCHAR2(30) := 'customerSalt';
  l_hash  VARCHAR2(128);
BEGIN
  SELECT LOWER(RAWTOHEX(STANDARD_HASH(
           UPPER(p_username) || l_salt || UPPER(p_password),
           'SHA1'           -->40 hex chars
         )))
    INTO l_hash
    FROM dual;

  RETURN l_hash;
END;
/
-- Check validity
SELECT object_name, status 
FROM user_objects 
WHERE object_name = 'GET_HASH';

create or replace procedure add_customer (
    p_username in customer.username%type,
    p_password in customer.password%type
)
AS
BEGIN
    insert into customer (custid, username, password)
    values (
        customer_seq.nextval,
        p_username,
        get_hash(p_username, p_password)
    );
end;

begin
    add_customer('adrian', 'hejhej');
end;

select get_hash('adrian','hejhej') from dual; 

create or replace function get_login(
    p_username in  varchar2,
    p_password in  varchar2
) return number
as
    v_count number;
BEGIN
    select count(*)
    into v_count
    from customer
    where username = p_username
        and password = get_hash(p_username, p_password);
    
    if v_count > 0 THEN
        return 1;
    else
        return 0;
     end if;
    end;

SELECT get_login('adrian', 'hejhej') AS login_result FROM dual;

-- Wrong password
SELECT get_login('adrian', 'wrongpass') AS login_result FROM dual;

-- Unknown username
SELECT get_login('notexists', 'hejhej') AS login_result FROM dual;

create or replace procedure change_password (
    p_username in customer.username%type,
    p_old_password in customer.password%type,
    p_new_password in customer.password%type,
    p_success out varchar2
)
AS
    l_old_password customer.PASSWORD%TYPE;
BEGIN
    select password
    into l_old_password
    from customer
    where username = p_username;

    if l_old_password = get_hash(p_username, p_old_password) THEN
    update CUSTOMER 
    set password = get_hash(p_username, p_new_password)
    where username = p_username;

    p_success := 'Password changed';
    else
        p_success := 'Invalid old password';
    end if;
 exception
     when no_data_found then
       p_success := 'Invalid username';
end change_password;

-- (If needed) add a test user
BEGIN
  add_customer('testuser', 'start123');
END;
/

-- Try changing with the correct old password
DECLARE
  v_msg VARCHAR2(100);
BEGIN
  change_password('testuser', 'start123', 'newpass123', v_msg);
  DBMS_OUTPUT.PUT_LINE(v_msg);
END;
/

-- Try changing with a wrong old password
DECLARE
  v_msg VARCHAR2(100);
BEGIN
  change_password('testuser', 'wrongpass', 'whatever', v_msg);
  DBMS_OUTPUT.PUT_LINE(v_msg);
END;
/

-- Verify row (hashed password)
SELECT username, password FROM customer WHERE username = 'testuser';

select * from customer;

create or replace package customer_security AS --spec
    procedure add_customer (
        p_username in customer.username%TYPE,
        p_password in varchar2
    );
    function get_login (
        p_username in customer.username%TYPE,
        p_password in varchar2
    ) return number;
    procedure change_password (
        p_username in customer.username%TYPE,
        p_old_password in varchar2,
        p_new_password in varchar2,
        p_success out varchar2
    );
end customer_security;

create or replace package body customer_security as --body
    function priv_get_hash (
        p_username in varchar2,
        p_password in varchar2
    ) return varchar2
    is
        l_hash  VARCHAR2(128);
        l_salt  CONSTANT VARCHAR2(30) := 'customerSalt';
    BEGIN
        SELECT LOWER(RAWTOHEX(
            STANDARD_HASH(
                UPPER(p_username) || l_salt || UPPER(p_password),
                'SHA1'           -->40 hex chars
                )
            ))
        INTO l_hash
        FROM dual;
        return l_hash;
    end priv_get_hash;

    procedure add_customer (
        p_username in customer.username%TYPE,
        p_password in varchar2
    ) IS
        l_hash VARCHAR2(128);
    BEGIN
        l_hash := priv_get_hash(p_username, p_password);
        insert into customer (custid, username, password)
    values (
        customer_seq.nextval,
        p_username,
        l_hash
    );
    exception
        when dup_val_on_index then
            raise_application_error(-20001, 'Username already exists.');
    end add_customer;

    function get_login (
        p_username in  customer.username%TYPE,
        p_password in  varchar2
    ) return number
    IS
        v_count number;
        l_hash  VARCHAR2(128);
    BEGIN
        l_hash := priv_get_hash(p_username, p_password);

        select count(*)
        into v_count
        from customer
        where username = p_username
        and password = l_hash;
        
        if v_count > 0 THEN
            return 1;
        else 
            return 0;
        end if;
    end get_login;

    procedure change_password (
        p_username in customer.username%TYPE,
        p_old_password in varchar2,
        p_new_password in varchar2,
        p_success out varchar2
    ) IS
        l_old_hash customer.password%TYPE;
        l_input_old  VARCHAR2(128);
        l_input_new  VARCHAR2(128);
    BEGIN
    l_input_old := priv_get_hash(p_username, p_old_password);
    l_input_new := priv_get_hash(p_username, p_new_password);
        select password
        into l_old_hash
        from customer
        where username = p_username;

    if l_old_hash = l_input_old THEN
        update CUSTOMER 
        set password = l_input_new
        where username = p_username;
        p_success := 'Password changed';
    ELSE
        p_success := 'Invalid old password';
    END IF;

    EXCEPTION
        WHEN NO_DATA_FOUND THEN
        p_success := 'Invalid username';
    END change_password;
end customer_security;   

-- Add a user via the package
BEGIN
  customer_security.add_customer('anna', 'ScruffyBeard');
END;
/

-- Check login
SELECT customer_security.get_login('anna', 'ScruffyBeard') AS ok FROM dual;  -- expect 1
SELECT customer_security.get_login('anna', 'ScryffyBear')  AS ok FROM dual;  -- expect 0

-- Change password
DECLARE
  v_msg VARCHAR2(100);
BEGIN
  customer_security.change_password('anna', 'ScruffyBeard', 'Scruffy', v_msg);
  DBMS_OUTPUT.PUT_LINE(v_msg);  -- expect 'Password changed'
END;
/

-- Verify new login works
SELECT customer_security.get_login('anna', 'Scruffy') AS ok FROM dual; -- expect 1