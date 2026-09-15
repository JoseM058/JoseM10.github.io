const menuButton = document.querySelector('.menu-button');
const navLinks = document.querySelector('.nav-links');
const themeButton = document.querySelector('.theme-button');

menuButton.addEventListener('click', () => {
  const open = navLinks.classList.toggle('open');
  menuButton.classList.toggle('active', open);
  menuButton.setAttribute('aria-expanded', String(open));
});

document.querySelectorAll('.nav-links a').forEach((link) => {
  link.addEventListener('click', () => {
    navLinks.classList.remove('open');
    menuButton.classList.remove('active');
    menuButton.setAttribute('aria-expanded', 'false');
  });
});

themeButton.addEventListener('click', () => {
  document.body.classList.toggle('light-hero');
});
