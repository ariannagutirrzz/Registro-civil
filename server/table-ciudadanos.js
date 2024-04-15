
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
  let ciudadanosData = null;

  axios.get('http://localhost:8000/Ciudadanos/read')
    .then((response) => { 
      ciudadanosData = response.data; 

      document.getElementById("body").innerHTML = ciudadanosData.map((ciudadano) => {
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

      const ciudadano = ciudadanosData[0]; // Obtén el primer ciudadano de la lista
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

