let cart = [];
let listProductHTML = document.querySelector('.listProduct');
let listCartHTML = document.querySelector('.listCart');
let iconCart = document.querySelector('.icon-cart');
let iconCartSpan = document.querySelector('.icon-cart span');
let body = document.querySelector('body');
let closeCart = document.querySelector('.close');
let products = [];

iconCart.addEventListener('click', () => {
    body.classList.toggle('showCart');
})
closeCart.addEventListener('click', () => {
    body.classList.toggle('showCart');
})

function addToCart(productId) {
    const productElement = document.querySelector(`.product[data-id="${productId}"]`);
    const productName = productElement.getAttribute('data-name');
    const productPrice = parseFloat(productElement.getAttribute('data-price'));

    const product = {
        id: productId,
        name: productName,
        price: productPrice
    };

    cart.push(product);
    updateCart();
}

function updateCart() {
    const cartElement = document.getElementById('cart');
    if (cart.length === 0) {
        cartElement.innerHTML = '<p>Корзина пуста</p>';
    } else {
        let cartItems = '<ul>';
        let total = 0;
        cart.forEach(item => {
            cartItems += `<li>${item.name} - ${item.price} руб.</li>`;
            total += item.price;
        });
        cartItems += '</ul>';
        cartItems += `<p><strong>Итого: ${total} руб.</strong></p>`;
        cartElement.innerHTML = cartItems;
    }
}