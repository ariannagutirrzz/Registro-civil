document.addEventListener("DOMContentLoaded", () => {
  const urlParams = new URLSearchParams(window.location.search);
  const cedula = urlParams.get("cedula");
  axios
    .get(`http://localhost:8000/Defunciones/read/${cedula}`)
    .then((response) => {
      console.log(response);
      const defuncion = response.data;
      document.getElementById("cedula").value = defuncion.cedula;
      document.getElementById("fecha_defuncion").value =
        defuncion.fecha_defuncion;
      document.getElementById("hora_defuncion").value =
        defuncion.hora_defuncion;
      document.getElementById("lugar_defuncion").value =
        defuncion.lugar_defuncion;
      document.getElementById("destino_cadaver").value =
        defuncion.destino_cadaver;
      document.getElementById("causa_defuncion").value =
        defuncion.causa_defuncion;
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
  const miForm = document.getElementById("modificar-defunciones");

  miForm.addEventListener("submit", (e) => {
    const urlParams = new URLSearchParams(window.location.search);
    const cedula = urlParams.get("cedula");
    e.preventDefault();

    const formData = new FormData(miForm);
    const jsonData = Object.fromEntries(formData);

    axios
      .put(`http://localhost:8000/Defunciones/update/${cedula}`, jsonData)
      .then((response) => {
        console.log(response);
        Swal.fire({
          icon: "success",
          title: "Modificado!",
          text: "La defuncion ha sido actualizada correctamente!",
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
          text: "Error al actualizar la defuncion",
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
