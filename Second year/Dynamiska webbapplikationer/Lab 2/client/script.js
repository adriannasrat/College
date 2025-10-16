async function getData() {
  const url = "http://localhost:3000/users";
  try {
    const response = await fetch(url)
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }
    const users = await response.json();
    printUsers(users);
    console.log(users);
  } catch (error) {
    console.error(error.message);
  }
}

function printUsers(users) {
  const userList = document.getElementById('userList');
  let html = `<ul class="mt-3 grid grid-cols-[repeat(auto-fit,_minmax(300px,_1fr))] gap-4">`;
  users.forEach((user) => {
    html += ` 
        <li
          class="bg-white p-3 w-fill flex flex-col rounded-md dark:bg-gray-800 shadow-lg relative ring-2 ring-${user.color}-500"
        >
          <div
            class="flex sm:flex-row flex-col items-center font-medium text-gray-900 dark:text-white pb-2 mb-2 sm:border-b border-gray-200 border-opacity-75 dark:border-gray-700 w-flil"
          >${user.firstName} ${user.lastName}
          </div>
          <div class="flex items-center w-fill">
            <div
              class="text-xs py-1 px-2 leading-none dark:bg-gray-900 bg-green-100 text-${user.color}-600 rounded-md"
            >
              @${user.username}
            </div>
            <div class="ml-auto text-xs text-gray-500">ID: ${user.id}</div>
          </div>
        </li>
      `;
  });

  userList.insertAdjacentHTML('beforeend', html);
}

getData();