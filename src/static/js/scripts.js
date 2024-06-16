function toggleText(container) {
  container.classList.add('active');
}

const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]')
const popoverList = [...popoverTriggerList].map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl))

$(document).ready(function () {

  // Script Login
  $('#loginForm').submit(function (event) {
    event.preventDefault();
    var formData = {
      'email': $('#email').val(),
    };

    var email = ($("#email").val())
    $.ajax({
      type: 'POST',
      url: '/login',
      data: JSON.stringify(formData),
      contentType: 'application/json',
      success: function (response) {
        $('#message').html(response.message);
        if (response.success) {
          $('#ModalLogin').modal('hide');
          $('#ModalLoginSucess').modal('show');
          setTimeout(function () {
            window.location.reload();
          }, 2000)
        } else {

          $('#ModalLogin').modal('hide');
          $('#ModalNewUser').modal('show');
        }
      },
      error: function (error) {
        console.log(error);
        $('#ModalLogin').modal('hide');
        $('#ModalError').modal('show');
      }
    });
  });


  // Script New User
  $('#NewUserForm').submit(function (event) {
    event.preventDefault();
    var formData = {
      'email': $('#email').val(),
      'NameUser': $('#NameUser').val()
    };
    $.ajax({
      type: 'POST',
      url: '/register',
      data: JSON.stringify(formData),
      contentType: 'application/json',
      success: function (response) {
        $('#ModalNewUser').modal('hide');
        $('#ModalLoginSucess').modal('show');
        setTimeout(function () {
          window.location.reload();
        }, 2000)
      },
      error: function (error) {
        console.log(error);
        $('#ModalNewUser').modal('hide');
        $('#ModalIncompleteName').modal('show');
        setTimeout(function () {
          $('#ModalIncompleteName').modal('hide');
          $('#ModalNewUser').modal('show');
        }, 1500)
      }
    });
  });


  // Script Logout
  $('#btn_logout').click(function () {
    $.ajax({
      type: 'POST',
      url: '/logout',
    });
    window.location.assign("/");
  });


});


// Modelos de Questões
(function ($) {
  const questoes = function () {

    /**
     * Get this question container element
     */
    let getQuestionContainer = function (prefix) {
      return $(`#${ prefix }-container`);
    };

    /**
     * Get a checkbox by its value
     * @param {string} value
     * @returns
     */
    let getCheckboxByValue = function (prefix, value) {
      const container = getQuestionContainer(prefix);
      return container.find(`input[type=checkbox][value="${ value }"], input[type=radio][value="${ value }"]`);
    };

    /**
     * Get a checkbox label element by the checkbox value
     * @param {string} value
     * @returns
     */
    let getCheckboxLabel = function (prefix, value) {
      const checkbox = getCheckboxByValue(prefix, value);
      return checkbox.siblings("label");
    };


    /**
     * Add style to the button by adding a CSS class to its label
     *
     * @param {string} prefix
     * @param {string} value  Valor do checkbox
     */
    let addStyle = function (prefix, value) {
      // check the checkboxes and style the button
      const checkbox = getCheckboxByValue(prefix, value);
      checkbox.prop("checked", true);
      // css styles
      const label = getCheckboxLabel(prefix, value);
      label.addClass("checked");
    };

    /**
     * Default the style of the button by removing the CSS class from it
     *
     * @param {string} prefix
     * @param {string} value  Valor do checkbox
     */
    let removeStyle = function (prefix, value) {
      const checkbox = getCheckboxByValue(prefix, value);
      checkbox.prop("checked", false);

      // css styles
      const label = getCheckboxLabel(prefix, value);
      label.removeClass("checked");
    };

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


    /**
     * Para questões com uma única escolha
     * @param {string} prefix  Prefixo/ID dessa lista de checkboxes
     * @param {Array} respostas  Array para guardar as respostas escolhidas
     */
    let choice = function (prefix, respostas) {
      $(`#${ prefix }a, #${ prefix }b, #${ prefix }c, #${ prefix }d, #${ prefix }e`).each(function () {
        $(this).on('click', function (event) {
          let value = respostas[ 0 ];
          let sel = getCheckboxByValue(prefix, value); // radio/checkboxes selecionados

          // uncheck todos checked
          removeStyle(prefix, sel.attr('value'));

          // add valor e style
          value = $(this).attr('value');
          respostas = [];
          respostas.push(value);
          addStyle(prefix, value);

          // console.log(prefix, respostas);
        });
      });
    }


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
          const container = getQuestionContainer(prefix);
          let nsel = container.find(`input[name^="${ prefix }"]:checked`).length; // numero de checkboxes selecionados

          // numero maximo de escolhas atingido
          if (nsel > maxSel) {
            // impede de selecionar mais opções
            return preventChanging(event);
          } else {
            if (Array.isArray(respostas)) {
              value = $(this).attr('value');

              // remove ou add a escolha à respostas
              let index = respostas.indexOf(value);
              if (index > -1) {
                // remove value
                respostas.splice(index, 1);
                removeStyle(prefix, value);
              } else {
                // add value
                respostas.push(value);
                addStyle(prefix, value);
              }

              if (typeof callback == "function") {
                callback(prefix, respostas)
              }
            }
          }
          // console.log(prefix, respostas)
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
      const container = getQuestionContainer(prefix);
      let inputs = container.find(`input[name^="${ prefix }-"]`);
      inputs.attr("value", null);

      inputs.each(function (index, input) {
        let option = respostas[ index ]
        let value = $(`#${ prefix }${ option }-label`).text();
        // console.log("valor:", value)

        $(input).attr("value", value);
      });
    };


    /**
     * Modelo de questões de associar duas colunas
     *
     * @param {string} prefix  Prefixo/ID dessa lista de checkboxes
     * @param {Object} respostas  Object Literal para guardar as respostas escolhidas
     */
    let assoc = function (prefix, respostas) {
      /**
       * Get the element that displays the associations made by the user
       * @returns
       */
      let getTextContainer = function () {
        return $(`#${ prefix }-associacoes p`);
      }

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

        addStyle(prefix, value);
        writeAssociations();
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
        removeStyle(prefix, inputValue1);
        removeStyle(prefix, inputValue2);
        writeAssociations();
      };

      /**
       * Mostra para o usuário as suas escolhas
       */
      let writeAssociations = function () {
        const pElem = getTextContainer();
        pElem.text("");

        for (key in respostas) {
          if (respostas.hasOwnProperty(key)) {
            if (key != "null" && respostas[ key ] != null) {
              const inputValue1 = key;
              const inputValue2 = respostas[ key ];
              const label1 = getCheckboxLabel(prefix, inputValue1);
              const label2 = getCheckboxLabel(prefix, inputValue2);
              const text1 = label1.text();
              const text2 = label2.text();
              pElem.append(`<span>${ text1 + " <i class='bi bi-arrow-left-right px-3'></i> " + text2 }</span>`);
              pElem.append("<br>");
            }
          }
        }
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
    };

    /**
     * Corrige as respostas do usuário
     *
     * Compara as respostas com o esperado. É esperado que os dois tenham o mesmo número de ítens
     * @param {Array|Object} respostas
     * @param {Array|Object} esperado
     * @returns {boolean} Se acertou ou não
     */
    let valida = function (respostas, esperado) {
      let estaCorreta = false;

      if (Array.isArray(esperado)) {
        estaCorreta = esperado.every((resp, index) => resp == respostas[ index ]);
      } else if (typeof esperado === 'object' && esperado !== null) {
        // Modelo 4 - object literal - dictionaries
        estaCorreta = true;
        for (const [ key, value ] of Object.entries(esperado)) {
          if (key in respostas == false || value != respostas[ key ]) {

            estaCorreta = false;
            break;
          }
        }
      } else {
        estaCorreta = esperado == respostas;
      }
      return estaCorreta;
    };


    /** Display popover to user */
    let displayPopover = function (totalCorrect, redirectUrl, redirectText = null) {
      const popup = $("#resultPopup");
      const overlay = $("#overlay");
      const popupContent = $("#popupContent");
      let redText = redirectText ?? "Ir para o Próximo conteúdo";

      popupContent.html(`
      <div class="card-cadastro1">
          <span class="titulo-cadastro">Parabéns!</span>
          <p class="mensagem-cadastro" style="margin-bottom: 20px">Você acertou um total de ${ totalCorrect } de 2 questões.</p>
          <div class="cadastro" style="display: flex;">
              <a href="${ redirectUrl }">
                  <button class="botao-enviar-email"> ${ redText }</button>
              </a>
              <a href="/">
                <button class="botao-enviar-email">Voltar para o início</button>
              </a>
          </div>
      </div>`);
      popup.css({ display: "block" })
      overlay.css({ display: "block" })
    }
    /** Close popup */
    $("#overlay").on('click', function () {
      // Close pop up
      const popup = $("#resultPopup");
      const overlay = $("#overlay");
      popup.css({ display: "none" })
      overlay.css({ display: "none" })
    });

    /**
     * Submit score to the server
     */
    let submitScore = function (data) {
      /*
      // Enviar para o servidor
      $.ajax({
        url: '/submit-score',
        method: 'POST',
        contentType: 'application/json',
        dataType: 'json',
        data: JSON.stringify(data),
        success: function (dataS, status, jqXHR) {
          // console.log('data', data)

          // Mostrar mensagem ao usuário
          displayPopover(dataS.totalCorrect);
        },
        error: function () {
          console.error('Erro ao enviar dados:', error);
        },
      });
      */
    }

    // public methods
    return {
      choice: choice,
      limitChoices: limitChoices,
      fillBlanks: fillBlanks,
      assoc: assoc,
      valida: valida,
      displayPopover: displayPopover,
      submitScore: submitScore,
    };
  }

  window.questoes = questoes();


})(this.jQuery);
// end Modelos de Questões
