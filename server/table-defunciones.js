const modalDelete = (cedula) => {
  Swal.fire({
    title: "¿Estás seguro de que quieres eliminar esto?",
    showCancelButton: true,
    confirmButtonText: "Sí, eliminar",
    confirmButtonColor: "#4caf50",
    denyButtonText: `No guardar`,
  }).then((result) => {
    if (result.isConfirmed) {
      axios
        .delete(`http://localhost:8000/Defunciones/delete/${cedula}`)
        .then((response) => {
          console.log(response);
          Swal.fire({
            icon: "success",
            title: "¡Eliminado!",
            text: "El ciudadano ha sido eliminado correctamente",
            position: "top-end",
            showConfirmButton: false,
            timer: 3000,
            toast: true,
            width: "30%",
            padding: "1em",
          }).then(() => {
            location.reload();
          });
        })
        .catch((error) => {
          console.error(error);
          Swal.fire({
            icon: "error",
            title: "Error",
            text: "Error al eliminar el ciudadano",
            position: "top-end",
            showConfirmButton: false,
            timer: 3000,
            toast: true,
            width: "30%",
            padding: "1em",
          });
        });
      Swal.fire("Deleted!", "", "success");
      location.reload();
    } else if (result.isDenied) {
      Swal.fire("Cambios no guardados", "", "info");
    }
  });
};

function modalCrearPDF(cedula) {
  Swal.fire({
    title: "¿Estás seguro de que quieres generar un PDF?",
    showCancelButton: true,
    confirmButtonText: "Sí, generar",
    confirmButtonColor: "#4caf50",
    denyButtonText: `No guardar`,
  }).then((result) => {
    if (result.isConfirmed) {
      axios
        .get(`http://localhost:8000/Defuncionespdf/read/${cedula}`)
        .then((response) => {
          console.log(response);
          const data = response.data;
          const pdf = new jsPDF();
          pdf.text(data, 10, 10);
          pdf.save("defuncion.pdf");
        });
      Swal.fire("PDF creado!", "", "success");
    } else if (result.isDenied) {
      Swal.fire("Cambios no guardados", "", "info");
    }
  });
}

document.addEventListener("DOMContentLoaded", () => {
  axios
    .get("http://localhost:8000/Defunciones/read")
    .then((response) => {
      document.getElementById("body").innerHTML = response.data
        .map((defuncion) => {
          return `
                    <tr>
                        <td>${defuncion.cedula || "Dato sin registrar"}</td>
                        <td>${
                          defuncion.fecha_defuncion || "Dato sin registrar"
                        }</td>
                        <td>${
                          defuncion.hora_defuncion || "Dato sin registrar"
                        } </td>
                        <td>${
                          defuncion.lugar_defuncion || "Dato sin registrar"
                        }</td>
                        <td>${
                          defuncion.destino_cadaver || "Dato sin registrar"
                        } </td>
                        <td>${
                          defuncion.causa_defuncion || "Dato sin registrar"
                        }</td>
                        <td><a href="/views/modificar/modificar-defuncion.html?cedula=${
                          defuncion.cedula
                        }" class="edit-button">Modificar</a></td>
                        <td><button onClick="modalDelete(${
                          defuncion.cedula
                        })" class="delete-button margin">Eliminar</button></td>
                        <td><button onClick="modalCrearPDF(${
                          defuncion.cedula
                        })" class="createPDF-button margin">Generar Certificado</button></td>
                    </tr>
                `;
        })
        .join("");
      console.log(response);
      Swal.fire({
        icon: "success",
        title: "¡Correcto!",
        text: "Datos mostrados correctamente",
        position: "top-end",
        showConfirmButton: false,
        timer: 3000,
        toast: true,
        width: "30%",
        padding: "1em",
      });
    })
    .catch((error) => {
      console.error(error);
      Swal.fire({
        icon: "error",
        title: "Error",
        text: "Error al mostrar los datos",
        position: "top-end",
        showConfirmButton: false,
        timer: 3000,
        toast: true,
        width: "30%",
        padding: "1em",
      });
    });
});
