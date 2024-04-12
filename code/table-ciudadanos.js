
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

const json = [{
    nombre: "Carlos",
    cedula: "123456789",
    sexo: "M",
    fecha_nacimiento: "2021-10-10",
},
{
    nombre: "Ari",
    cedula: "30605255",
    sexo: "F",
    fecha_nacimiento: "2004-06-08",
},
{
    nombre: "Luis",
    cedula: "123456789",
}
];

document.getElementById("body").innerHTML = json.map((ciudadano) => {
    return `
        <tr>
            <td>${ciudadano.nombre || "Dato sin registrar"}</td>
            <td>${ciudadano.cedula || "Dato sin registrar"}</td>
            <td>${ciudadano.sexo || "Dato sin registrar"} </td>
            <td>${ciudadano.fecha_nacimiento || "Dato sin registrar"}</td>
            <td><button onClick="modal(${ciudadano.cedula})" class="back-button">Eliminar</button></td>
        </tr>
    `;
}).join("");