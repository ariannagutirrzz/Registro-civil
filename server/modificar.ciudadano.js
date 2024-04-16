document.addEventListener("DOMContentLoaded", () => {
  const urlParams = new URLSearchParams(window.location.search);
  const cedula = urlParams.get("cedula");
  axios
    .get(`http://localhost:8000/Ciudadanos/read/${cedula}`)
    .then((response) => {
      console.log(response);
      const ciudadano = response.data[0];
      document.getElementById("cedula").value = ciudadano.cedula;
      document.getElementById("nacionalidad").value = ciudadano.nacionalidad;
      document.getElementById("estado_civil").value = ciudadano.estado_civil;
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
  const miForm = document.getElementById("modificar-ciudadanos");

  miForm.addEventListener("submit", (e) => {
    const urlParams = new URLSearchParams(window.location.search);
    const cedula = urlParams.get("cedula");
    e.preventDefault();

    const formData = new FormData(miForm);
    const jsonData = Object.fromEntries(formData);

    axios
      .put(`http://localhost:8000/Ciudadanos/update/${cedula}`, jsonData)
      .then((response) => {
        console.log(response);
        Swal.fire({
          icon: "success",
          title: "Modificado!",
          text: "El ciudadano ha sido actualizado correctamente!",
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
          text: "Error al actualizar el ciudadano",
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
