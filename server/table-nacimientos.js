const modalDelete = (id) => {
    Swal.fire({
        title: "Are you sure you want to delete this?",
        showDenyButton: true,
        showCancelButton: true,
        confirmButtonText: "Yes, delete it",
        denyButtonText: `Don't save`
      }).then((result) => {
        /* Read more about isConfirmed, isDenied below */
        if (result.isConfirmed) {
            axios.delete(`http://localhost:8000/Nacimientos/delete/${id}`)
            .then((response) => {
              console.log(response);
              alert("Nacimiento eliminado correctamente");
            })
            .catch((error) => {
              console.error(error);
              alert("Error al eliminar un Nacimiento");
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
    axios.get("http://localhost:8000/Nacimientos/read")
          .then((response) => {
            document.getElementById("body").innerHTML = response.data.map((nacimiento) => {
                return `
                    <tr>
                        <td>${nacimiento.id}</td>
                        <td>${nacimiento.nombre || "Dato sin registrar"}</td>
                        <td>${nacimiento.sexo || "Dato sin registrar"} </td>
                        <td>${nacimiento.fecha_nacimiento || "Dato sin registrar"}</td>
                        <td>${nacimiento.hora_nacimiento || "Dato sin registrar"}</td>
                        <td>${nacimiento.lugar_nacimiento || "Dato sin registrar"}</td>
                        <td>${nacimiento.padre1_cedula || "Dato sin registrar"}</td>
                        <td>${nacimiento.padre2_cedula || "Dato sin registrar"}</td>
                        <td>${nacimiento.testigo1_cedula || "Dato sin registrar"}</td>
                        <td>${nacimiento.testigo2_cedula || "Dato sin registrar"}</td>
                        <td>${nacimiento.parroquia || "Dato sin registrar"}</td>
                        <td><button onClick="modalDelete(${nacimiento.id})" class="back-button">Eliminar</button></td>
                        <td><button onClick="modalUpdate(${nacimiento.id})" class="back-button">Modificar</button></td>
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
