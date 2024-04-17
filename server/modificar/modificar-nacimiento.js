document.addEventListener("DOMContentLoaded", () => {
  const urlParams = new URLSearchParams(window.location.search);
  const table_id = urlParams.get("table_id");
  axios
    .get(`http://localhost:8000/Nacimientos/read/${table_id}`)
    .then((response) => {
      console.log(response);
      const nacimiento = response.data;
      document.getElementById("nombre").value = nacimiento.nombre;
      document.getElementById("sexo").value = nacimiento.sexo;
      document.getElementById("fecha_nacimiento").value =
        nacimiento.fecha_nacimiento;
      document.getElementById("hora_nacimiento").value =
        nacimiento.hora_nacimiento;
      document.getElementById("lugar_nacimiento").value =
        nacimiento.lugar_nacimiento;
      document.getElementById("padre1_cedula").value = nacimiento.padre1_cedula;
      document.getElementById("padre2_cedula").value = nacimiento.padre2_cedula;
      document.getElementById("testigo1_cedula").value =
        nacimiento.testigo1_cedula;
      document.getElementById("testigo2_cedula").value =
        nacimiento.testigo2_cedula;
      document.getElementById("parroquia").value = nacimiento.parroquia;
    })
    .catch((error) => {
      console.error(error, "error");
      Swal.fire({
        icon: "error",
        title: "Error",
        text: "Error al mostrar los datos",
        heightAuto: false,
        customClass: {
          popup: "half-size",
        },
      });
    });
});

document.addEventListener("DOMContentLoaded", () => {
  const miForm = document.getElementById("modificar-nacimientos");

  miForm.addEventListener("submit", (e) => {
    const urlParams = new URLSearchParams(window.location.search);
    const table_id = urlParams.get("table_id");
    e.preventDefault();

    const formData = new FormData(miForm);
    const jsonData = Object.fromEntries(formData);

    axios
      .put(`http://localhost:8000/Nacimientos/update/${table_id}`, jsonData)
      .then((response) => {
        console.log(response);
        Swal.fire({
          icon: "success",
          title: "Modificado!",
          text: "El nacimiento ha sido actualizado correctamente!",
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
          text: "Error al actualizar el nacimiento",
          position: "top-end",
          showConfirmButton: false,
          timer: 3000,
          toast: true,
          width: "30%",
          padding: "1em",
        });
      });
  });
});
