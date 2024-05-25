function toggleText(container) {
  container.classList.toggle('active');
}


$(document).ready(function () {
  /**
   * Limita o número de opções escolhidas em uma lista de checkboxes
   *
   * @param {int} maxSel  Número máximo de opções que podem ser escolhidas
   * @param {string} prefix  Prefixo/ID dessa lista de checkboxes
   * @param {Array} respostas  Array para guardar as respostas escolhidas
   * @param {callable} callback (Optional) Callback function executada sempre que a respostas é alterada
   */
  let limitChoices = function (maxSel, prefix, respostas, callback = null) {
    $(`#${ prefix }a, #${ prefix }b, #${ prefix }c, #${ prefix }d, #${ prefix }e`).each(function () {
      // on click event of a checkbox
      $(this).on('click', function (event) {
        let container = $(`#${ prefix }-container`);
        let nsel = container.find(`input[name^="${ prefix }"]:checked`).length; // numero de checkboxes selecionados

        // numero maximo de escolhas atingido
        if (nsel > maxSel) {
          // impede de selecionar mais opções
          event.stopPropagation();
          return false;
        } else {
          if (Array.isArray(respostas)) {
            value = $(this).attr('value');

            // remove ou add a escolha à respostas
            let index = respostas.indexOf(value);
            if (index > -1) {
              // remove value
              respostas.splice(index, 1);
            } else {
              // add value
              respostas.push(value);
            }

            if (typeof callback == "function") {
              callback(prefix, respostas)
            }
          }
        }
        // console.log(respostas)
      });
    });
  };

  /**
   * Preenche as lacunas de uma questão
   *
   * @param {string} prefix  Prefixo/ID dessa lista de checkboxes
   * @param {Array} respostas  Array para guardar as respostas escolhidas
   */
  let fillBlanks = function (prefix, respostas) {
    let inputs = $(`#${ prefix }-container input[name^="${ prefix }-"]`)
    inputs.attr("value", null);

    inputs.each(function (index, input) {
      let option = respostas[ index ]
      let value = $(`#${ prefix }${ option }-label`).text();
      // console.log("valor:", value)

      $(input).attr("value", value);
    });
  };


  /**
   *
   *
   * @param {string} prefix  Prefixo/ID dessa lista de checkboxes
   * @param {Object} respostas  Object Literal para guardar as respostas escolhidas
   */
  let assoc = function (prefix, respostas) {

    /**
     * Add valor as respostas.
     *
     * Se existir um valor nulo na mesma coluna, substitui o valor nulo.
     * @param value Valor a ser add
     * @param {int} column column 1 corresponde a key de `respostas`, coluna 2 corresponde ao value de `respostas`
     */
    let add = function (value, column) {
      if (column == 1) {
        if (respostas[ null ]) {
          respostas[ value ] = respostas[ null ];
          delete respostas[ null ];
        } else {
          respostas[ value ] = null;
        }
      } else if (column == 2) {
        found = null;
        for (let key in respostas) {
          if (respostas.hasOwnProperty(key)) {
            if (respostas[ key ] == null) {
              found = key;
            }
          }
        }
        respostas[ found ] = value;
      }

      addStyle(value);
      escreveAssociacoes();
    };

    /**
     * Remove uma escolha de `respostas`
     *
     * @param value Valor a ser removido
     * @param {int} column column 1 corresponde a key de `respostas`, coluna 2 corresponde ao value de `respostas`
     */
    let remove = function (value, column) {
      inputValue1 = null;
      inputValue2 = null;

      if (column == 1) {
        inputValue1 = value;
        inputValue2 = respostas[ value ];

        delete respostas[ value ];
      } else if (column == 2) {
        // se achar o valor nas respostas, apaga
        for (let key in respostas) {
          if (respostas.hasOwnProperty(key)) {
            if (respostas[ key ] == value) {
              inputValue1 = key;
              inputValue2 = respostas[ key ];

              delete respostas[ key ];
            }
          }
        }
      }

      // uncheck the checkboxes and style the button
      removeStyle(inputValue1);
      removeStyle(inputValue2);
      escreveAssociacoes();
    };

    /**
     * Mostra para o usuário as suas escolhas
     */
    let escreveAssociacoes = function () {
      const pElem = getTextContainer();
      pElem.text("");

      for (key in respostas) {
        if (respostas.hasOwnProperty(key)) {
          if (key != "null" && respostas[ key ] != null) {
            const inputValue1 = key;
            const inputValue2 = respostas[ key ];
            const label1 = getCheckboxLabel(inputValue1);
            const label2 = getCheckboxLabel(inputValue2);
            const text1 = label1.text();
            const text2 = label2.text();
            pElem.append(`<span>${ text1 + " <i class='bi bi-arrow-left-right px-3'></i> " + text2 }</span>`);
            pElem.append("<br>");
          }
        }
      }
    };

    /**
     * Add style to the button by adding a CSS class to its label
     *
     * @param {string} prefix
     * @param {string} value  Valor do checkbox
     */
    let addStyle = function (value) {
      // check the checkboxes and style the button
      const checkbox = getCheckboxByValue(value);
      checkbox.prop("checked", true);
      // css styles
      const label = getCheckboxLabel(value);
      label.addClass("checked");
    };

    /**
     * Default the style of the button by removing the CSS class from it
     *
     * @param {string} prefix
     * @param {string} value  Valor do checkbox
     */
    let removeStyle = function (value) {
      const checkbox = getCheckboxByValue(value);
      checkbox.prop("checked", false);

      // css styles
      const label = getCheckboxLabel(value);
      label.removeClass("checked");
    };

    /**
      * Verifica se valor existe em respostas (key|value)
      *
      * @param value Valor a ser verificado
      * @param {int} column column 1 corresponde a key de `respostas`, coluna 2 corresponde ao value de `respostas`
      */
    let exists = function (value, column) {
      if (column == 1) {
        // Procura nas keys de respostas

        return (value in respostas);
      } else if (column == 2) {
        // Procura nos values de respostas
        found = false;
        for (let key in respostas) {
          if (respostas.hasOwnProperty(key)) {
            if (respostas[ key ] == value) {
              found = true;
              break;
            }
          }
        }

        return found;
      }

      return null;
    };


    /**
     * Get this question container element
     */
    let getQuestionContainer = function () {
      return $(`.${ prefix }-container`);
    };

    /**
     * Get a checkbox by its value
     * @param {string} value
     * @returns
     */
    let getCheckboxByValue = function (value) {
      const container = getQuestionContainer();
      return container.find(`input[type=checkbox][value="${ value }"]`);
    };

    /**
     * Get a checkbox label element by the checkbox value
     * @param {string} value
     * @returns
     */
    let getCheckboxLabel = function (value) {
      const checkbox = getCheckboxByValue(value);
      return checkbox.siblings("label");
    };

    /**
     * Get the element that displays the associations made by the user
     * @returns
     */
    let getTextContainer = function () {
      return $(`#${ prefix }-associacoes p`);
    }

    /**
     * Impede botão de ser selecionado
     *
     * @param event
     * @returns bool
     */
    let preventChanging = function (event) {
      event.stopPropagation();
      return false;
    };


    $(`#${ prefix }a1, #${ prefix }b1, #${ prefix }c1, #${ prefix }d1, #${ prefix }e1, ` +
      `#${ prefix }a2, #${ prefix }b2, #${ prefix }c2, #${ prefix }d2, #${ prefix }e2`).each(function () {

        // on click event of a checkbox
        $(this).on('click', function (event) {
          let column = this.id?.slice(-1);
          let otherColumn = column == 1 ? 2 : 1;
          let value = $(this).attr("value");
          // console.log(
          //   'column', column,
          //   'value', value,
          //   'existe:', exists(null, column)
          // )

          if (exists(value, column)) {      // se existe uma key|value (na mesma coluna) com seu valor.
            // remove
            remove(value, column);
          } else if (exists(null, column)) { // se existe uma key|value (na mesma coluna) nulo
            // add a escolha(substitui o valor nulo)
            add(value, column);
            // troca a cor - .btn: focus - visible
          } else if (exists(null, otherColumn)) {  // se existe uma key|value (na outra coluna) nulo
            // impede de selecionar a escolha
            return preventChanging(event);
          } else {
            // add a escolha (add com o seu par(key|value) sendo nulo)
            add(value, column);
            // troca a cor - .btn:focus-visible
          }

          // console.log(respostas);
        });
      });
  }

  /* Questões Modelo: 2 altenativas corretas - checkbox */
  const respostasQ2 = []
  limitChoices(2, 'q2', respostasQ2);

  /* Questões Modelo 3: 2 altenativas corretas - completar lacunas */
  const respostasQ3 = []
  limitChoices(2, 'q3', respostasQ3, fillBlanks);

  /** Questões Modelo 4: Associar colunas */
  const respostasQ4 = {};
  assoc('q4', respostasQ4);
});
