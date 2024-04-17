document.addEventListener("DOMContentLoaded", () => {
  const urlParams = new URLSearchParams(window.location.search);
  const table_id = urlParams.get("table_id");
  axios
    .get(`http://localhost:8000/Matrimonios/read/${table_id}`)
    .then((response) => {
      console.log(response);
      const matrimonio = response.data;
      document.getElementById("contrayente1_cedula").value =
        matrimonio.contrayente1_cedula;
      document.getElementById("contrayente2_cedula").value =
        matrimonio.contrayente2_cedula;
      document.getElementById("contrayente1_padre1_cedula").value =
        matrimonio.contrayente1_padre1_cedula;
      document.getElementById("contrayente1_padre2_cedula").value =
        matrimonio.contrayente1_padre2_cedula;
      document.getElementById("contrayente2_padre1_cedula").value =
        matrimonio.contrayente2_padre1_cedula;
      document.getElementById("contrayente2_padre2_cedula").value =
        matrimonio.contrayente2_padre2_cedula;
      document.getElementById("fecha_ActaMatrimonio").value =
        matrimonio.fecha_ActaMatrimonio;
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
  const miForm = document.getElementById("modificar-matrimonio");

  miForm.addEventListener("submit", (e) => {
    const urlParams = new URLSearchParams(window.location.search);
    const table_id = urlParams.get("table_id");
    e.preventDefault();

    const formData = new FormData(miForm);
    const jsonData = Object.fromEntries(formData);

    axios
      .put(`http://localhost:8000/Matrimonios/update/${table_id}`, jsonData)
      .then((response) => {
        console.log(response);
        Swal.fire({
          icon: "success",
          title: "Modificado!",
          text: "El matrimonio ha sido actualizado correctamente!",
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
          text: "Error al actualizar el matrimonio",
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
