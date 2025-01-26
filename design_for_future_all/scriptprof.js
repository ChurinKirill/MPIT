        window.addEventListener('load', () => {
            setTimeout(() => {
                document.querySelector('.loader').style.display = 'none';
                document.querySelector('.content').style.display = 'block';

                document.addEventListener('mousemove', (e) => {
                    if (Math.random() > 0.9) { // Adjust the frequency of coin creation
                        const coin = document.createElement('div');
                        coin.className = 'coin';
                        coin.style.left = `${e.pageX}px`;
                        coin.style.top = `${e.pageY}px`;
                        coin.style.setProperty('--random-x', `${Math.random() * 200 - 10}`);
                        document.body.appendChild(coin);
                        setTimeout(() => {
                            coin.remove();
                        }, 1000);
                    }
                });
            }, 1000);
        });