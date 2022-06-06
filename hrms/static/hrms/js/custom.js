function customerListingsDetails(pump_opening_price,quantity_of_concrete_cube,concrete_cube_price,paid,employee){

    // FORMULAE   = opening price of the pump + (amount of concrete cube -10) * cprice per cube of oncrete.
    var price = parseInt(pump_opening_price) +parseInt(parseInt(quantity_of_concrete_cube)-10)*parseInt(concrete_cube_price)
    console.log(price);
    var VAT =price *0.17
    document.getElementById('customerPriceWithoutVAT').innerHTML =price
    document.getElementById('customerPriceWithVAT').innerHTML =price + VAT
    document.getElementById('employeeiddd').value =employee

    console.log(paid);
    if(paid =='False'){
        console.log(paid);
        document.getElementById("paid").className = "notPaid";
        document.getElementById("paid").className += "";

        document.getElementById("paid").innerHTML = 'Not Paid'
    }else{
        document.getElementById("paid").className = "paid";
        document.getElementById("paid").className += "";

        document.getElementById("viewUpdate").className += "hddi";
        

        document.getElementById("paid").innerHTML = 'Paid'
    }

    console.log('done')

}