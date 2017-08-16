$( document ).ready(function() {
    var users = [];
    var consumption = [];

    $(".cons_users").each(function( index ) {
        users.push($(this).text())
    });

    $(".cons_consumption").each(function( index ) {
        consumption.push($(this).text())
    });

    var ctx = document.getElementById("myChart").getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: users,
            datasets: [{
                data: consumption,
                label: "Consumption",
                fill: false
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            title: {
                display: true,
                text: 'Total Consumption Across all Users'
            }
        }

    });
});