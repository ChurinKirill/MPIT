function getCart() {
    return JSON.parse(localStorage.getItem('cart')) || [];
}

function saveCart(cart) {
    localStorage.setItem('cart', JSON.stringify(cart));
}

// Функции для главной страницы
function addToCart(id, name, price) {
    const cart = getCart();
    const existingItem = cart.find(item => item.id === id);
    
    if (existingItem) {
        existingItem.quantity++;
    } else {
        cart.push({ id, name, price, quantity: 1 });
    }
    
    saveCart(cart);
    
}

// Функции для страницы корзины
function updateCartDisplay() {
    const cart = getCart();
    const cartItems = document.getElementById('cart-items');
    const totalPrice = document.getElementById('total-price');
    
    cartItems.innerHTML = '';
    let total = 0;
    
    cart.forEach(item => {
        total += item.price * item.quantity;
        const itemElement = document.createElement('div');
        itemElement.className = 'cart-item';
        itemElement.innerHTML = `
            <span>${item.name} x${item.quantity}</span>
            <span>${item.price * item.quantity} ₽</span>
            <button onclick="removeItem(${item.id})">×</button>
        `;
        cartItems.appendChild(itemElement);
    });
    
    totalPrice.textContent = `Общая сумма: ${total} ₽`;
}

function removeItem(id) {
    let cart = getCart();
    cart = cart.filter(item => item.id !== id);
    saveCart(cart);
    updateCartDisplay();
}

function clearCart() {
    localStorage.removeItem('cart');
    updateCartDisplay();
}

// Инициализация корзины при загрузке страницы
if (window.location.pathname.endsWith('cart.html')) {
    updateCartDisplay();
}