let burger_btn = document.getElementById('burger-btn')
let window_burger = document.getElementById('burger-menu')
let burg_btn_close = document.getElementById('burg-btn-close')

burger_btn.addEventListener('click', function() {
window_burger.style.display = 'block';
this.style.setProperty('display', 'none', 'important');
burg_btn_close.style.display = 'block';

});


burg_btn_close.addEventListener('click', function() {
burger_btn.style.display = 'block';
window_burger.style.display = 'none';
burg_btn_close.style.display = 'none';
});

const anchors = document.querySelectorAll('a[href*="#"]')

for (let anchor of anchors) {
  anchor.addEventListener('click', function (e) {
    e.preventDefault()

    const blockID = anchor.getAttribute('href').substr(1)

    document.getElementById(blockID).scrollIntoView({
      behavior: 'smooth',
      block: 'start'
    })
  })
}