$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})

$('.dropdown-toggle').dropdown()

$('.carousel').carousel()

$(function () {
  $("#formulario").validate({
    rules: {
      nombre: {
        required: true
      },
      apellido: {
        required: true
      },
      correo: {
        required: true
      },
      telefono: {
        required: true
      },
      asunto: {
        required: true
      },
      mensaje: {
        required: true
      }
    },
    messages: {
      nombre: {
        required: "Ingrese nombre",
      },
      apellido: {
        required: "Ingrese apellido",
      },
      correo: {
        required: "Ingrese email",
        email: "Debe ingresar un correo con formato abc@abc.cl"
      },
      telefono: {
        required: "Ingrese numero telefonico",
      },
      asunto: {
        required: "Ingrese asusnto",
      },
      mensaje: {
        required: "Ingrese mensaje"
      }
    }
  })
})

$(document).ready(function(){
	$('#telefono').mask('9 99 99 99 99');
});

$('.alert').alert()