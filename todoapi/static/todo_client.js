const API_URL = '/api/tasks/';
const taskListDiv = document.getElementById('task-list');
const taskForm = document.getElementById('task-form');

// --- POBIERANIE i WYŚWIETLANIE ZADAŃ (GET) ---
async function fetchTasks() {
  try {
    const response = await fetch(API_URL);
    const data = await response.json();
    renderTasks(data.tasks);
  } catch (error) {
    console.error('Błąd podczas pobierania zadań:', error);
    taskListDiv.innerHTML =
      '<p style="color: red;">Nie udało się załadować listy zadań z API.</p>';
  }
}

function renderTasks(tasks) {
  taskListDiv.innerHTML = '';
  tasks.forEach((task) => {
    const isDone = task.done;
    const item = document.createElement('div');
    item.className = `task-item ${isDone ? 'completed' : ''}`;
    item.id = `task-${task.id}`;

    item.innerHTML = `
                    <span class="task-title">${task.title}</span>
                    <div class="actions">
                        ${
                          !isDone
                            ? `<button data-id="${task.id}" class="done-btn">Zakończ (PATCH)</button>`
                            : '<span>Wykonane</span>'
                        }
                        <button data-id="${
                          task.id
                        }" class="delete-btn">Usuń (DELETE)</button>
                    </div>
                `;
    taskListDiv.appendChild(item);
  });
  attachEventListeners();
}

// --- OBSŁUGA DODAWANIA ZADAŃ (POST) ---
taskForm.addEventListener('submit', async (e) => {
  e.preventDefault();
  const title = document.getElementById('task-input').value;

  try {
    const response = await fetch(API_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ title: title }),
    });

    if (response.status === 201) {
      document.getElementById('task-input').value = '';
      fetchTasks();
    }
  } catch (error) {
    console.error('Błąd sieci przy dodawaniu zadania:', error);
  }
});

// --- OBSŁUGA AKTUALIZACJI/USUWANIA (PATCH/DELETE) ---
function attachEventListeners() {
  // Obsługa oznaczania jako wykonane (PATCH)
  document.querySelectorAll('.done-btn').forEach((button) => {
    button.addEventListener('click', async (e) => {
      const taskId = e.target.dataset.id;

      try {
        const response = await fetch(`${API_URL}${taskId}/done/`, {
          method: 'PATCH',
        });

        if (response.ok) {
          fetchTasks();
        }
      } catch (error) {
        console.error('Błąd aktualizacji statusu:', error);
      }
    });
  });

  // Obsługa usuwania (DELETE)
  document.querySelectorAll('.delete-btn').forEach((button) => {
    button.addEventListener('click', async (e) => {
      const taskId = e.target.dataset.id;

      if (!confirm('Czy na pewno chcesz usunąć to zadanie?')) return;

      try {
        const response = await fetch(`${API_URL}${taskId}/`, {
          method: 'DELETE',
        });

        if (response.status === 204) {
          fetchTasks();
        }
      } catch (error) {
        console.error('Błąd usuwania zadania:', error);
      }
    });
  });
}

fetchTasks();
