const modalDelete = (table_id) => {
  Swal.fire({
    title: "¿Estás seguro de que quieres eliminar esto?",
    showCancelButton: true,
    confirmButtonText: "Sí, eliminar",
    confirmButtonColor: "#4caf50",
    denyButtonText: `No guardar`,
  }).then((result) => {
    if (result.isConfirmed) {
      axios
        .delete(`http://localhost:8000/Nacimientos/delete/${table_id}`)
        .then((response) => {
          console.log(response);
          Swal.fire({
            icon: "success",
            title: "¡Eliminado!",
            text: "El nacimiento ha sido eliminado correctamente",
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
            text: "Error al eliminar el nacimiento",
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

function modalCrearPDF(id) {
  Swal.fire({
    title: "¿Estás seguro de que quieres generar un PDF?",
    showCancelButton: true,
    confirmButtonText: "Sí, generar",
    confirmButtonColor: "#4caf50",
    denyButtonText: `No guardar`,
  }).then((result) => {
    if (result.isConfirmed) {
      axios
        .get(`http://localhost:8000/Nacimientospdf/read/${id}`)
        .then((response) => {
          console.log(response);
          const data = response.data;
          const pdf = new jsPDF();
          pdf.text(data, 10, 10);
          pdf.save("nacimiento.pdf");
        });
      Swal.fire("PDF creado!", "", "success");
    } else if (result.isDenied) {
      Swal.fire("Cambios no guardados", "", "info");
    }
  });
}

document.addEventListener("DOMContentLoaded", () => {
  axios
    .get("http://localhost:8000/Nacimientos/read")
    .then((response) => {
      document.getElementById("body").innerHTML = response.data
        .map((nacimiento) => {
          return `
                      <tr>
                      <td>${nacimiento.id || "Dato sin registrar"}</td>
                          <td>${nacimiento.nombre || "Dato sin registrar"}</td>
                          <td>${nacimiento.sexo || "Dato sin registrar"} </td>
                          <td>${
                            nacimiento.fecha_nacimiento || "Dato sin registrar"
                          }</td>
                          <td>${
                            nacimiento.hora_nacimiento || "Dato sin registrar"
                          }</td>
                          <td>${
                            nacimiento.lugar_nacimiento || "Dato sin registrar"
                          }</td>
                          <td>${
                            nacimiento.padre1_cedula || "Dato sin registrar"
                          }</td>
                          <td>${
                            nacimiento.padre2_cedula || "Dato sin registrar"
                          }</td>
                          <td>${
                            nacimiento.testigo1_cedula || "Dato sin registrar"
                          }</td>
                          <td>${
                            nacimiento.testigo2_cedula || "Dato sin registrar"
                          }</td>
                          <td>${
                            nacimiento.parroquia || "Dato sin registrar"
                          }</td>
                          <td><a href="/views/modificar/modificar-nacimiento.html?table_id=${
                            nacimiento.id
                          }" class="edit-button">Modificar</a></td>

                          <td><button onClick="modalDelete(${
                            nacimiento.id
                          })" class="delete-button margin">Eliminar</button></td>

                          <td><button onClick="modalCrearPDF(${
                            nacimiento.id
                          })" class="createPDF-button margin">Generar PDF</button></td>
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
