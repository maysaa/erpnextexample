$(document).ready(function() {
		//e.preventDefault();
	var customer_name="";
	var item_name="";
	var description="";
	var Company_name="";
	var account_name="";

      	var data= $.getJSON('http://0.0.0.0:8000/api/resource/Item/?fields=["item_name","description","website_image"]',function(data){
      		//alert(data);
			$.each(data, function(key,value) {
			  alert(data[key]);
			});
			var obj = data.data[0];
                item_name = obj.item_name;
                description = obj.description;
                $("#item"+1).html(item_name);
                $("#descr"+1).html(description);
                $("#image"+1).attr("src", obj.website_image);
			 var obj1 = data.data[1];
                item_name = obj1.item_name;
                description = obj1.description;
                $("#item2").html(item_name)
                $("#descr2").html(description)
                $("#image2").attr("src", obj1.website_image)
			 // var obj2 = data.data[2];
              //   item_name = obj2.item_name;
              //   description = obj2.description;
              //   $("#item3").html(item_name)
              //   $("#descr3").html(description)
              //   $("#image3").attr("src", ob2.website_image)
			 // var obj3 = data.data[4];
              //   item_name = obj3.item_name;
              //   description = obj3.description;
              //   $("#item4").html(item_name)
              //   $("#descr4").html(description)
              //   $("#image4").attr("src", obj3.website_image)

			});

			var data= $.getJSON('http://0.0.0.0:8000/api/resource/Customer/?fields=["customer_name"]',function(data){
      		customer_name= data.data[0].customer_name;
      		});

			$('#buy_btn').click(function(e) {
				e.preventDefault();
				var post={"data":JSON.stringify({"customer":customer_name,"delivery_date":"28-12-2016",
					"items":[{
                "item_code": item_name,
                "item_name": item_name,
                "description": description,
				"qty": "1.0"
            	}]})};
				$.post("http://0.0.0.0:8000/api/resource/Sales Order",post,function(result){
				alert("Success adding Sales Order");
				});

				var data= $.getJSON('http://0.0.0.0:8000/api/resource/Company/?fields=["company_name"]',function(data){
      		    Company_name= data.data[0].name;
				});

				var data= $.getJSON('http://0.0.0.0:8000/api/resource/Account/?fields=["name"]',function(data){
      		    account_name= data.data[0].name;});

				var post={"data":JSON.stringify({"customer":customer_name,"company":"exa","due_date":"28-12-2016","debit_to":account_name,
					"items":[{
                "item_name": item_name,
                "description": description,
                "income_account": "Sales - E",
				"qty": "1.0",
				"rate":"20.0"
            	}]})};
				$.post("http://0.0.0.0:8000/api/resource/Sales Invoice",post,function(result){
				alert("Success adding Sales Invoice");
				});

            });

});







// $(document).ready(function() {
//     $('#save').click(function(e) {
// 		e.preventDefault();
// 		var first_name= $("#firstname").val();
// 		var redirect_to= $("#lastname").val();
// 		var full_name= $("#username").val();
// 		var email= $("#email").val();
// 		var bio= $("#bio").val();
// 		var post={"email":email,"full_name":full_name,"redirect_to":redirect_to};
// $.post("http://0.0.0.0:8000/api/method/frappe.core.doctype.user.user.sign_up",post,function(result){
// alert("Success11");
// });
//
// 	});
//
//     });

