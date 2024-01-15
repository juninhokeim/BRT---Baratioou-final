document.addEventListener("DOMContentLoaded", function () {
    var toggleButton = document.getElementById("toggleCategories");
    var categoriesMenu = document.getElementById("categoriesMenu");
    var body = document.body;

    toggleButton.addEventListener("click", function (event) {
        // Alternar a visibilidade do menu de categorias
        if (categoriesMenu.style.display === "none" || categoriesMenu.style.display === "") {
            categoriesMenu.style.display = "block";
            body.classList.add("categories-active"); // Adiciona a classe 'categories-active' ao body
        } else {
            categoriesMenu.style.display = "none";
            body.classList.remove("categories-active"); // Remove a classe 'categories-active' do body
        }
        event.stopPropagation(); // Impede a propagação do clique para que não feche imediatamente ao clicar no botão
    });

    // Adiciona um ouvinte de eventos de clique ao corpo do documento
    document.addEventListener("click", function (event) {
        // Verifica se o clique ocorreu fora do menu de categorias
        if (!categoriesMenu.contains(event.target) && event.target !== toggleButton) {
            categoriesMenu.style.display = "none";
            body.classList.remove("categories-active"); // Remove a classe 'categories-active' do body
        }
    });
});