// Funkcja do pobierania tokena CSRF (konieczna dla POST/DELETE)
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.startsWith(name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

const csrftoken = getCookie('csrftoken');

document.addEventListener('DOMContentLoaded', () => {
  // 1. GŁOSOWANIE (LIKOWANIE) - AJAX POST
  document.querySelectorAll('.vote-btn').forEach((button) => {
    button.addEventListener('click', async (e) => {
      const eventId = e.currentTarget.dataset.eventId;
      const voteSpan = document.getElementById(`votes-${eventId}`);

      if (!eventId) {
        alert('Błąd: Brak ID wydarzenia do głosowania.');
        return;
      }

      try {
        // Żądanie POST do endpointu API
        const response = await fetch(`/events/api/events/${eventId}/vote/`, {
          method: 'POST',
          headers: {
            'X-CSRFToken': csrftoken,
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({}),
        });

        if (response.ok) {
          const data = await response.json();
          voteSpan.textContent = data.new_votes; // Aktualizuj licznik
          e.currentTarget.disabled = true;
        } else {
          alert(`Głosowanie nie powiodło się! Status: ${response.status}.`);
        }
      } catch (error) {
        console.error('Network Error:', error);
      }
    });
  });

  // 2. USUWANIE WYDARZENIA - AJAX DELETE
  document.querySelectorAll('.delete-btn').forEach((button) => {
    button.addEventListener('click', async (e) => {
      const eventId = e.currentTarget.dataset.eventId;

      if (
        !confirm(
          'Czy na pewno chcesz USUNĄĆ to wydarzenie i wszystkie powiązane dane?'
        )
      ) {
        return;
      }

      try {
        // Wysłanie żądania DELETE do API
        const response = await fetch(`/events/api/events/${eventId}/delete/`, {
          method: 'DELETE',
          headers: {
            'X-CSRFToken': csrftoken,
          },
        });

        if (response.status === 204) {
          // 204 No Content
          // Usuwamy element z widoku, używając unikalnego ID
          const eventPost = document.getElementById(`event-post-${eventId}`);
          if (eventPost) {
            eventPost.remove();
          }
          alert('Wydarzenie zostało usunięte.');
        } else {
          alert(
            `Błąd: Nie udało się usunąć wydarzenia. Status: ${response.status}`
          );
        }
      } catch (error) {
        console.error('Network Error:', error);
      }
    });
  });

  // 3. LOGIKA POKAZYWANIA KOMENTARZY
  document.querySelectorAll('.comment-toggle-btn').forEach((button) => {
    button.addEventListener('click', (e) => {
      const eventId = e.currentTarget.dataset.eventId;
      const commentsSection = document.getElementById(`comments-${eventId}`);

      if (commentsSection) {
        commentsSection.style.display =
          commentsSection.style.display === 'none' ? 'block' : 'none';
      }
    });
  });
});
