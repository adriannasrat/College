#!/bin/bash

create_group() {
  local grp
  while true; do
    read -rp "Enter a new group name: " grp
    [[ -z "$grp" ]] && { echo "Group name cannot be empty."; continue; }

    if getent group "$grp" >/dev/null 2>&1; then
      echo "Group '$grp' already exists. Try another." >&2
    else
      groupadd "$grp"
      echo "Group '$grp' has been created." >&2
      echo "$grp"   # return via stdout
      return 0
    fi
  done
}

prompt_username_unique() {
  local uname
  while true; do
    read -rp "Enter new username: " uname
    [[ -z "$uname" ]] && { echo "Username cannot be empty."; continue; }

    if id -u "$uname" >/dev/null 2>&1; then
      echo "User '$uname' already exists. Try another." >&2
    else
      echo "$uname"  # return via stdout
      return 0
    fi
  done
}

prompt_password_confirm() {
  local p1 p2
  while true; do
    read -rs -p "Enter password: " p1; echo >&2
    read -rs -p "Confirm password: " p2; echo >&2
    if [[ -z "$p1" ]]; then
      echo "Password cannot be empty." >&2
    elif [[ "$p1" != "$p2" ]]; then
      echo "Passwords do not match. Try again." >&2
    else
      echo "$p1"   # return via stdout
      return 0
    fi
  done
}

setup_department_dir() {
  local user="$1"
  local grp="$2"
  local dir="/$user"

  mkdir -p "$dir"

  chown "$user:$grp" "$dir"

  chmod 3770 "$dir"

  echo
  echo "==== Department Directory Verification ===="
  echo "Directory: $dir"

  ls -ld "$dir"

  stat -c 'Mode: %A (%a) Owner: %U Group: %G' "$dir"
  echo "User info:"
  id "$user"
  echo "Group info:"
  getent group "$grp" | cut -d: -f1-4
  echo
}

create_user_in_group() {
  local grp="$1"
  local username password

  username="$(prompt_username_unique)"
  password="$(prompt_password_confirm)"

  useradd -m -s /bin/bash -g "$grp" "$username"
  echo "$username:$password" | chpasswd

  echo "Created user '$username' with Bash shell and added to group '$grp'."

  setup_department_dir "$username" "$grp"
}

main() {
  # (Run script with sudo)
  local group_name
  group_name="$(create_group)"
  create_user_in_group "$group_name"
}

main