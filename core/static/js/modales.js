const openModal = document.querySelector('.nueva_mascota');
const modal = document.querySelector('.modal');
const closeModal = document.querySelector('.modal_close');




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
  }
});

document.onload(document.getElementById('MascotasForm').reset());