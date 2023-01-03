$(document).ready(function () {
    // Init
    $('.image-section').hide();
    $('.loader').hide();
    $('#result').hide();

    // Upload Preview
    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.readAsDataURL(input.files[0]);
        }
    }

    $("#imageUpload").change(function () {
        $('.image-section').show();
        $('#btn-predict').show();
        $('#result').empty().hide();
        readURL(this);
    });

    // Predict
    $('#btn-predict').click(function () {
        var form_data = new FormData($('#upload-file')[0]);

        // Show loading animation
        $(this).hide();
        $('.loader').show();

        // Make prediction by calling api /predict
        $.ajax({
            type: 'POST',
            url: '/predict',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: true,
            success: function (data) {
                if (data['state'] == 'SUCCESS') {
                    // Get and display the result and hide loader
                    $('.loader').hide();
                    $('#result').fadeIn(600);

                    $('#result').append("<h3>Uploaded image:</h3>")
                    $('#result').append(`<img src='/static/uploads/${data.file_name}.jpg' width='400' alt='File name: ${data.file_name}'>`)

                    $('#result').append("<hr>")
                    $('#result').append(`<p>Document name: ${data.file_name}.</p>`)
    
                    $('#result').append("<h3>Top 3 predicted labels with its probabilities:</h3>")
                    $('#result').append("<hr>")

                    data.preds.forEach((pred, row) => {
                        $('#result').append(`<p>${(row + 1).toString()}. ${pred.label} with ${(100*pred.prob).toFixed(2)}% probability.</p>`)
                    })

                    console.log('Classified Successfully!');

                } else if(data['state'] == 'FAILURE') {
                    // Hide loader
                    $('.loader').hide();
                    
                    // Show Error notification for 5s.
                    $(".notify").addClass("active");
                    setTimeout(function(){
                        $(".notify").removeClass("active");
                    }, 5000);

                }
            },
        });
    });
});
