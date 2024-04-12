
const modal = (cedula) => {
    Swal.fire({
        title: "Are you sure you want to delete this?",
        showDenyButton: true,
        showCancelButton: true,
        confirmButtonText: "Yes, delete it",
        denyButtonText: `Don't save`
      }).then((result) => {
        /* Read more about isConfirmed, isDenied below */
        if (result.isConfirmed) {
            axios.delete(`http://localhost:3000/Ciudadanos/delete/${cedula}`)
          Swal.fire("Deleted!", "", "success");
          location.reload();

        } else if (result.isDenied) {
          Swal.fire("Changes are not saved", "", "info");
        }
      });
}

// const json = [{
//     nombre: "Carlos",
//     cedula: "123456789",
//     sexo: "M",
//     fecha_nacimiento: "2021-10-10",
// },
// {
//     nombre: "Ari",
//     cedula: "30605255",
//     sexo: "F",
//     fecha_nacimiento: "2004-06-08",
// },
// {
//     nombre: "Luis",
//     cedula: "123456789",
// }
// ];

document.addEventListener("DOMContentLoaded", (e) => {
    //   const miForm = document.getElementById("form-ciudadanos");
    axios.get("http://localhost:8000/Ciudadanos/read")
          .then((response) => {
            document.getElementById("body").innerHTML = response.data.map((ciudadano) => {
                return `
                    <tr>
                        <td>${ciudadano.cedula || "Dato sin registrar"}</td>
                        <td>${ciudadano.nacionalidad || "Dato sin registrar"}</td>
                        <td>${ciudadano.estado_civil || "Dato sin registrar"} </td>
                        <td>${ciudadano.nacimientos_id || "Dato sin registrar"}</td>
                        <td><button onClick="modal(${ciudadano.cedula})" class="back-button">Eliminar</button></td>
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
