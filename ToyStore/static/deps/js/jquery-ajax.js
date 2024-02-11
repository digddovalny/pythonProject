
$(document).ready(function () {
    var successMessage = $("#jq-notification");

     $(document).on("click", ".add-to-basket", function (e) {
         e.preventDefault();

         var goodsInBasketCount = $("#goods-in-basket-count");
         var basketCount = parseInt(goodsInBasketCount.text() || 0);

         var product_id = $(this).data("product-id");

         var add_to_basket_url = $(this).attr("href");

         $.ajax({
             type: "POST",
             url: add_to_basket_url,
             data: {
                 product_id: product_id,
                 csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
             },
             success: function (data) {
                 successMessage.html(data.message);
                 successMessage.fadeIn(400);
                 setTimeout(function () {
                     successMessage.fadeOut(400);
                 }, 4000);

                 basketCount++;
                 goodsInBasketCount.text(basketCount);

                 var basketItemsContainer = $("#basket-items-container");
                 basketItemsContainer.html(data.basket_items_html);

             },

             error: function (data) {
                 console.log("Ошибка при добавлении товара в корзину");
             },
         });
     });




     $(document).on("click", ".remove-from-basket", function (e) {
         e.preventDefault();

         var goodsInBasketCount = $("#products-in-basket-count");
         var basketCount = parseInt(goodsInBasketCount.text() || 0);

         var basket_id = $(this).data("basket-id");
         var remove_from_basket = $(this).attr("href");

         $.ajax({

             type: "POST",
             url: remove_from_basket,
             data: {
                 basket_id: basket_id,
                 csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
             },
             success: function (data) {
                 successMessage.html(data.message);
                 successMessage.fadeIn(400);
                 setTimeout(function () {
                     successMessage.fadeOut(400);
                 }, 4000);

                 basketCount -= data.quantity_deleted;
                 goodsInBasketCount.text(basketCount);

                 var basketItemsContainer = $("#basket-items-container");
                 basketItemsContainer.html(data.basket_items_html);

             },

             error: function (data) {
                 console.log("Ошибка при добавлении товара в корзину");
             },
         });
     });




     $(document).on("click", ".decrement", function () {
         var url = $(this).data("basket-change-url");
         var basketID = $(this).data("basket-id");
         var $input = $(this).closest('.input-group').find('.number');
         var currentValue = parseInt($input.val());
         if (currentValue > 1) {
             $input.val(currentValue - 1);
             updateBasket(basketID, currentValue - 1, -1, url);
         }
     });

     $(document).on("click", ".increment", function () {
         var url = $(this).data("basket-change-url");
         var basketID = $(this).data("basket-id");
         var $input = $(this).closest('.input-group').find('.number');
         var currentValue = parseInt($input.val());

         $input.val(currentValue + 1);

         updateBasket(basketID, currentValue + 1, 1, url);
     });

     function updateBasket(basketID, quantity, change, url) {
         $.ajax({
             type: "POST",
             url: url,
             data: {
                 basket_id: basketID,
                 quantity: quantity,
                 csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
             },
 
             success: function (data) {
                 successMessage.html(data.message);
                 successMessage.fadeIn(400);
                 setTimeout(function () {
                      successMessage.fadeOut(400);
                 }, 4000);

                 var goodsInBasketCount = $("#products-in-basket-count");
                 var basketCount = parseInt(goodsInBasketCount.text() || 0);
                 basketCount += change;
                 goodsInBasketCount.text(basketCount);

                 var basketItemsContainer = $("#basket-items-container");
                 basketItemsContainer.html(data.basket_items_html);

             },
             error: function (data) {
                 console.log("Ошибка при добавлении товара в корзину");
             },
         });
     }

    var notification = $('#notification');
    if (notification.length > 0) {
        setTimeout(function () {
            notification.alert('close');
        }, 4000);
    }

    $('#modalButton').click(function () {
        $('#exampleModal').appendTo('body');

        $('#exampleModal').modal('show');
    });

    $('#exampleModal .btn-close').click(function () {
        $('#exampleModal').modal('hide');
    });

    $("input[name='requires_delivery']").change(function() {
        var selectedValue = $(this).val();
        if (selectedValue === "1") {
            $("#deliveryAddressField").show();
        } else {
            $("#deliveryAddressField").hide();
        }
    });
});