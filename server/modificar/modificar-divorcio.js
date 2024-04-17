document.addEventListener("DOMContentLoaded", () => {
  const urlParams = new URLSearchParams(window.location.search);
  const table_id = urlParams.get("table_id");
  axios
    .get(`http://localhost:8000/Divorcios/read/${table_id}`)
    .then((response) => {
      console.log(response);
      const divorcio = response.data;
      document.getElementById("divorciado1_cedula").value =
        divorcio.divorciado1_cedula;
      document.getElementById("divorciado2_cedula").value =
        divorcio.divorciado2_cedula;
      document.getElementById("fecha_ActaDivorcio").value =
        divorcio.fecha_ActaDivorcio;
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
  const miForm = document.getElementById("modificar-divorcios");

  miForm.addEventListener("submit", (e) => {
    const urlParams = new URLSearchParams(window.location.search);
    const table_id = urlParams.get("table_id");
    e.preventDefault();

    const formData = new FormData(miForm);
    const jsonData = Object.fromEntries(formData);

    axios
      .put(`http://localhost:8000/Divorcios/update/${table_id}`, jsonData)
      .then((response) => {
        console.log(response);
        Swal.fire({
          icon: "success",
          title: "Modificado!",
          text: "El divorcio ha sido actualizado correctamente!",
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
          text: "Error al actualizar el divorcio",
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
