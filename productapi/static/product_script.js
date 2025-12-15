async function fetchProducts() {
  const resultsDiv = document.getElementById('product-results');
  resultsDiv.innerHTML = '<p>Ładowanie danych...</p>';

  try {
    const response = await fetch('products/');

    if (!response.ok) {
      throw new Error(`Błąd HTTP: ${response.status}`);
    }

    const data = await response.json();

    displayProducts(data);
  } catch (error) {
    console.error('Błąd podczas pobierania produktów:', error);
    resultsDiv.innerHTML = `<p class="error">Wystąpił błąd: ${error.message}</p>`;
  }
}

function displayProducts(products) {
  const resultsDiv = document.getElementById('product-results');

  if (products.length === 0) {
    resultsDiv.innerHTML = '<p>Lista produktów jest pusta.</p>';
    return;
  }

  let html = '<h2>Lista Produktów (JSON Response)</h2>';
  html += '<ul class="product-list">';

  products.forEach((product) => {
    const stockClass = product.in_stock ? 'in-stock' : 'out-of-stock';
    const stockText = product.in_stock ? 'Dostępny' : 'Brak';

    html += `
                    <li class="product-item">
                        <span class="product-name">${product.name}</span>
                        <span class="product-price">${product.price.toFixed(
                          2
                        )} PLN</span>
                        <span class="product-stock ${stockClass}">${stockText}</span>
                    </li>
                `;
  });

  html += '</ul>';
  resultsDiv.innerHTML = html;
}
