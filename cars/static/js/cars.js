$(document).ready(function () {
    const updateBtn = $('#update-btn');
    const saveBtn = $('#save-btn');
    const form = $('#cars-form');

    function recalculateTotalValue() {
        let sum = 0;
        $(this).parent().parent().parent().children().find(".sum-value").each(function () {
            sum += parseInt($(this).val());
        })
        $(this).parent().parent().parent().children().find(".total-value").text(`$ ${sum}`);
    }


    function toggleEditability(editable) {
        const disableValue = (editable === true);
        $('table tbody tr td:not(:last-child)').each(function () {
            $(this).children().children().prop("disabled", !disableValue);
        });
    }

    updateBtn.click(function () {
        if (updateBtn.text() === "Cancel") {
            location.reload();
        }
        saveBtn.show();
        updateBtn.text("Cancel");
        updateBtn.addClass("btn-danger");
        updateBtn.removeClass("btn-primary");
        toggleEditability(true);
    });

    saveBtn.click(function () {
        form.submit();
    });

    toggleEditability(false);
    $(".sum-value").on("change", recalculateTotalValue);
    $(".total-value").each(function () {
        recalculateTotalValue.call(this);
    });
});