
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

// const modalUpdate = (cedula) => {
//     Swal.fire({
//         title: "Are you sure you want to update this?",
//         showDenyButton: true,
//         showCancelButton: true,
//         confirmButtonText: "Yes, update it",
//         denyButtonText: `Don't save`
//       }).then((result) => {
//         /* Read more about isConfirmed, isDenied below */
//         if (result.isConfirmed) {
//             axios.put(`http://localhost:8000/Ciudadanos/update/${cedula}`)
//             .then((response) => {
//               console.log(response);
//               alert("Ciudadano actualizado correctamente");
//             })
//             .catch((error) => {
//               console.error(error);
//               alert("Error al actualizar un ciudadano");
//             });
//           Swal.fire("Updated!", "", "success");
//           location.reload();

//         } else if (result.isDenied) {
//           Swal.fire("Changes are not saved", "", "info");
//         }
//       });
// }

// json = [{
//     cedula: "123456789",
//     nacionalidad: "V",
//     estado_civil: "Soltero",
//     nacimientos_id: 1
// }]

document.addEventListener("DOMContentLoaded", () => {
    axios.get("http://localhost:8000/Ciudadanos/read")
          .then((response) => {
            document.getElementById("body").innerHTML = response.data.map((ciudadano) => {
                return `
                    <tr>
                        <td>${ciudadano.cedula || "Dato sin registrar"}</td>
                        <td>${ciudadano.nacionalidad || "Dato sin registrar"}</td>
                        <td>${ciudadano.estado_civil || "Dato sin registrar"} </td>
                        <td>${ciudadano.nacimientos_id || "Dato sin registrar"}</td>
                        <td><button onClick="modalDelete(${ciudadano.cedula})" class="back-button">Eliminar</button></td>
                        <td><button onClick="modalUpdate(${ciudadano.cedula})" class="back-button">Modificar</button></td>
                    </tr>
                `;
            }).join("");
            console.log(response);
            alert("Datos mostrados correctamente");
          })
          .catch((error) => {
            console.error(error);
            alert("Error al mostrar los datos");
          });
      });

// Editar formularios

document.addEventListener("DOMContentLoaded", () => {
  axios.get("http://localhost:8000/Ciudadanos/read")
      .then((response) => {
          // Rellenar los campos del formulario con los datos obtenidos
          document.getElementById("estado_civil").value = response.data.estado_civil;
          // Rellenar otros campos del formulario
      })
      .catch((error) => {
          console.error(error);
          alert("Error al cargar los datos del ciudadano");
      });
});



document.addEventListener("DOMContentLoaded", () => {
  axios.get("http://localhost:8000/Ciudadanos/read")
        .then((response) => {
          document.getElementById("body").innerHTML = response.data.map((ciudadano) => {
              return `
                  <tr>
                      <td>${ciudadano.cedula || "Dato sin registrar"}</td>
                      <td>${ciudadano.nacionalidad || "Dato sin registrar"}</td>
                      <td>${ciudadano.estado_civil || "Dato sin registrar"} </td>
                      <td>${ciudadano.nacimientos_id || "Dato sin registrar"}</td>
                      <td><button onClick="modalDelete(${ciudadano.cedula})" class="back-button">Eliminar</button></td>
                      <td><button onClick="modalUpdate(${ciudadano.cedula})" class="back-button">Modificar</button></td>
                  </tr>
              `;
          }).join("");
          console.log(response);
          alert("Datos mostrados correctamente");
        })
        .catch((error) => {
          console.error(error);
          alert("Error al mostrar los datos");
        });
    });
