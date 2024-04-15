
const modalDelete = (table_id) => {
    Swal.fire({
        title: "Are you sure you want to delete this?",
        showDenyButton: true,
        showCancelButton: true,
        confirmButtonText: "Yes, delete it",
        denyButtonText: `Don't save`
      }).then((result) => {
        /* Read more about isConfirmed, isDenied below */
        if (result.isConfirmed) {
            axios.delete(`http://localhost:8000/Divorcios/delete/${table_id}`)
            .then((response) => {
              console.log(response);
              alert("Divorcio eliminado correctamente");
            })
            .catch((error) => {
              console.error(error);
              alert("Error al eliminar un divorcio");
            });
          Swal.fire("Deleted!", "", "success");
          location.reload();

        } else if (result.isDenied) {
          Swal.fire("Changes are not saved", "", "info");
        }
      });
}

document.addEventListener("DOMContentLoaded", () => {
    axios.get("http://localhost:8000/Divorcios/read")
          .then((response) => {
            document.getElementById("body").innerHTML = response.data.map((divorcio) => {
                return `
                    <tr>
                        <td>${divorcio.id}</td>
                        <td>${divorcio.divorciado1_cedula || "Dato sin registrar"}</td>
                        <td>${divorcio.divorciado2_cedula || "Dato sin registrar"}</td>
                        <td>${divorcio.fecha_ActaDivorcio || "Dato sin registrar"} </td>
                        <td><button onClick="modalDelete(${divorcio.id})" class="back-button">Eliminar</button></td>
                        <td><button onClick="modalUpdate(${divorcio.id})" class="back-button">Modificar</button></td>
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
