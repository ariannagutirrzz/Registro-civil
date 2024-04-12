
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
            axios.delete(`http://localhost:8000/Matrimonios/delete/${id}`)
            .then((response) => {
              console.log(response);
              alert("Matrimonio eliminado correctamente");
              location.reload();
            })
            .catch((error) => {
              console.error(error);
              alert("Error al eliminar un matrimonio");
            });
        } else if (result.isDenied) {
          Swal.fire("Changes are not saved", "", "info");
        }
      });
}
document.addEventListener("DOMContentLoaded", () => {
    axios.get("http://localhost:8000/Matrimonios/read")
          .then((response) => {
            console.log(response);
            document.getElementById("body").innerHTML = response.data.map((matrimonio) => {
                return `
                    <tr>
                        <td>${matrimonio.id}</td>
                        <td>${matrimonio.contrayente1_cedula || "Dato sin registrar"}</td>
                        <td>${matrimonio.contrayente2_cedula || "Dato sin registrar"}</td>
                        <td>${matrimonio.contrayente1_padre1_cedula || "Dato sin registrar"} </td>
                        <td>${matrimonio.contrayente1_padre2_cedula || "Dato sin registrar"}</td>
                        <td>${matrimonio.contrayente2_padre1_cedula || "Dato sin registrar"}</td>
                        <td>${matrimonio.contrayente2_padre2_cedula || "Dato sin registrar"}</td>
                        <td>${matrimonio.fecha_ActaMatrimonio || "Dato sin registrar"}</td>
                        <td><button onClick="modalDelete(${matrimonio.id})" class="back-button">Eliminar</button></td>
                        <td><button onClick="modalUpdate(${matrimonio.id})" class="back-button">Modificar</button></td>
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
