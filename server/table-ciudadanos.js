
const modalDelete = (cedula) => {
    Swal.fire({
        title: "Are you sure you want to delete this?",
        showDenyButton: true,
        showCancelButton: true,
        confirmButtonText: "Yes, delete it",
        denyButtonText: `Don't save`
      }).then((result) => {
        /* Read more about isConfirmed, isDenied below */
        if (result.isConfirmed) {
            axios.delete(`http://localhost:8000/Ciudadanos/delete/${cedula}`)
            .then((response) => {
              console.log(response);
              alert("Ciudadano eliminado correctamente");
            })
            .catch((error) => {
              console.error(error);
              alert("Error al eliminar un ciudadano");
            });
          Swal.fire("Deleted!", "", "success");
          location.reload();

        } else if (result.isDenied) {
          Swal.fire("Changes are not saved", "", "info");
        }
      });
}
document.addEventListener("DOMContentLoaded", () => {
  axios.get('http://localhost:8000/Ciudadanos/read')
    .then((response) => { 
      document.getElementById("body").innerHTML = response.data.map((ciudadano) => {
        return `
          <tr>
            <td>${ciudadano.cedula || "Dato sin registrar"}</td>
            <td>${ciudadano.nacionalidad || "Dato sin registrar"}</td>
            <td>${ciudadano.estado_civil || "Dato sin registrar"} </td>
            <td>${ciudadano.nacimientos_id || "Dato sin registrar"}</td>
            <td><button onClick="modalDelete(${ciudadano.cedula})" class="back-button">Eliminar</button></td>
            <td><a href="../modificar/modificar-ciudadano.html?cedula=${ciudadano.cedula}">Modificar</a></td>
          </tr>
        `;
      }).join("");

      const ciudadano = response.data[0];
      document.getElementById("cedula").value = ciudadano ? ciudadano.cedula : "Dato sin registrar";
      document.getElementById("nacionalidad").value = ciudadano ? ciudadano.nacionalidad : "Dato sin registrar";
      document.getElementById("estado_civil").value = ciudadano ? ciudadano.estado_civil : "Dato sin registrar";

      console.log(response);
      alert("Datos mostrados correctamente");
    })
    .catch((error) => {
      console.error(error);
      alert("Error al mostrar los datos");
    });
});

      // document.addEventListener("DOMContentLoaded", () => {
      //   axios.get("http://localhost:8000/Ciudadanos/read/${cedula}")
      //     .then((response) => {
      //       const ciudadano = response.data[0]; // Obtener el primer objeto del arreglo
      //       document.getElementById("body").innerHTML = `
      //         <tr>
      //           <td>${ciudadano.cedula || "Dato sin registrar"}</td>
      //           <td>${ciudadano.nacionalidad || "Dato sin registrar"}</td>
      //           <td>${ciudadano.estado_civil || "Dato sin registrar"}</td>
      //           <td>${ciudadano.nacimientos_id || "Dato sin registrar"}</td>
      //           <td><button onClick="modalDelete('${ciudadano.cedula}')" class="back-button">Eliminar</button></td>
      //           <td><a href="../modificar/modificar-ciudadano.html?cedula=${ciudadano.cedula}">Modificar</a></td>
      //         </tr>`;
      //       console.log(response);
      //       alert("Datos mostrados correctamente");
      //     })
      //     .catch((error) => {
      //       console.error(error);
      //       alert("Error al mostrar los datos");
      //     });
      // });
      
// Editar formularios

// document.addEventListener("DOMContentLoaded", () => {
//   axios.get("http://localhost:8000/Ciudadanos/read")
//       .then((response) => {
//           // Rellenar los campos del formulario con los datos obtenidos
//           document.getElementById("cedula").value = response.data.cedula;
//           document.getElementById("nacionalidad").value = response.data.nacionalidad;
//           document.getElementById("estado_civil").value = response.data.estado_civil;

//           // Rellenar otros campos del formulario
//       })
//       .catch((error) => {
//           console.error(error);
//           alert("Error al cargar los datos del ciudadano");
//       });
// });
