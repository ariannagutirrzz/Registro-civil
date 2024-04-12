
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
            axios.delete(`http://localhost:8000/Defunciones/delete/${id}`)
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
    axios.get("http://localhost:8000/Defunciones/read")
          .then((response) => {
            document.getElementById("body").innerHTML = response.data.map((defuncion) => {
                return `
                    <tr>
                        <td>${defuncion.cedula || "Dato sin registrar"}</td>
                        <td>${defuncion.fecha_defuncion || "Dato sin registrar"}</td>
                        <td>${defuncion.hora_defuncion || "Dato sin registrar"} </td>
                        <td>${defuncion.lugar_defuncion || "Dato sin registrar"}</td>
                        <td>${defuncion.destino_cadaver || "Dato sin registrar"} </td>
                        <td>${defuncion.causa_defuncion || "Dato sin registrar"}</td>
                        <td><button onClick="modalDelete(${defuncion.id})" class="back-button">Eliminar</button></td>
                        <td><button onClick="modalUpdate(${defuncion.id})" class="back-button">Modificar</button></td>
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
