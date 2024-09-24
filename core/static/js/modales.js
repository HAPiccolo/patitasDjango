const openModal = document.querySelector('.nueva_mascota');
const modal = document.querySelector('.modal');
const closeModal = document.querySelector('.modal_close');


const modal_modificar_mascota = document.querySelector('.modificar_mascota');
const mod_mascota = document.querySelector('.mod_mascota');

openModal.addEventListener('click', () => {

  modal.classList.add('modal--show');

});

closeModal.addEventListener('click', () => {

  modal.classList.remove('modal--show');
});

// Evento para cerrar el modal sin guardar los datos

document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape') {
    modal.classList.remove('modal--show');
    mod_mascota.classList.remove('modal--show');
  }
});


modal_modificar_mascota.addEventListener('click', () => {
  mod_mascota.classList.add('modal--show');
});
