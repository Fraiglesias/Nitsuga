/*!
* Start Bootstrap - Agency v7.0.12 (https://startbootstrap.com/theme/agency)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-agency/blob/master/LICENSE)
*/
//
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    // Navbar shrink function
    var navbarShrink = function () {
        const navbarCollapsible = document.body.querySelector('#mainNav');
        if (!navbarCollapsible) {
            return;
        }
        if (window.scrollY === 0) {
            navbarCollapsible.classList.remove('navbar-shrink')
        } else {
            navbarCollapsible.classList.add('navbar-shrink')
        }

    };

    // Shrink the navbar 
    navbarShrink();

    // Shrink the navbar when page is scrolled
    document.addEventListener('scroll', navbarShrink);

    //  Activate Bootstrap scrollspy on the main nav element
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            rootMargin: '0px 0px -40%',
        });
    };

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });


});

function agregarAlCarrito(id, nombre, precio) {
    let carrito = JSON.parse(localStorage.getItem('carrito')) || [];
    carrito.push({'id': id, 'nombre': nombre, 'precio': precio});
    localStorage.setItem('carrito', JSON.stringify(carrito));
    Swal.fire({
        title: "",
        text: "Producto agregado!",
        icon: "success"
    });
};

function mostrarCarrito() {
    let carrito = JSON.parse(localStorage.getItem('carrito')) || [];

    if (carrito.length === 0) {
      Swal.fire({
        title: 'Carrito Vacío',
        text: 'No hay productos en tu carrito.',
        icon: 'info',
      });
      return;
    } else {
        let contenidoTabla = `
          <table class="table table-striped">
            <thead>
              <tr>
                <th scope="col">Producto</th>
                <th scope="col">Precio</th>
                <th scope="col">Acciones</th>
              </tr>
            </thead>
            <tbody>
        `;
        carrito.forEach((val, index) => {
          contenidoTabla += `
              <tr>
                <td>${val['nombre']}</td>
                <td>${val['precio']}</td>
                <td>
                  <button onclick="eliminarDelCarrito(${index})" class="btn btn-danger btn-sm">
                    Eliminar
                  </button>
                </td>
              </tr>
          `;
        });
        contenidoTabla += `
            </tbody>
          </table>
          <hr>
          <button class="btn btn-success btn-block" onclick="comprar()">Comprar</button>
        `;
    
        Swal.fire({
          title: 'Tu Carrito',
          html: contenidoTabla,
          showCloseButton: true,
          showConfirmButton: false,
        });
    }
  }

function eliminarDelCarrito(index) {
    let carrito = JSON.parse(localStorage.getItem('carrito')) || [];
    carrito.splice(index, 1);
    localStorage.setItem('carrito', JSON.stringify(carrito));

    mostrarCarrito();
}

function comprar() {
  const cliente_id = localStorage.getItem('cliente_id');
  console.log(localStorage);
  if (cliente_id === 'None') {
    Swal.fire({
      title: "¡Ups!",
      text: "Necesitar estar con una sesión iniciada, identificate!",
      icon: "info",
    });
  } else {

    const carrito = JSON.parse(localStorage.getItem('carrito'));
    const productos_ids = carrito.map(producto => parseInt(producto.id));
    let productos_precio_total = carrito.map(producto => parseInt(producto.precio));

    let suma = 0;
    for (const numero of productos_precio_total) {
      suma += numero;
    }

    $.ajax({
        url: '/crear_pedido/',
        type: 'POST',
        data: {
            'cliente_id': cliente_id,
            'productos_ids': JSON.stringify(productos_ids),
            'productos_precio_total': suma,
            'csrfmiddlewaretoken': csrftoken
        },
        success: function(response) {
            Swal.fire({
              title: "¡Gracias por tu compra!",
              text: "Tu pedido está siendo procesado. Pronto nos contactaremos contigo por correo!",
              icon: "success",
            });
  
            localStorage.removeItem('carrito');
  
            console.log(response);
        },
        error: function(error) {
            Swal.fire({
              title: "¡Oh no!",
              text: "Ocurrió un problema al realizar la compra, intentalo de nuevo!",
              icon: "error",
            });
  
            console.error(error);
        }
    });
  }
};


function cerrar_sesion() {
  localStorage.removeItem('cliente_id');
};