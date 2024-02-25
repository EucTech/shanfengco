// $(document).ready(function () {
//     $('#messages').click(function (event) {
//         $('.admin-message').show();
//         $('.admin-newsletter').hide();
//         $('.admin-send-newsletter').hide();
//         $('#messages').addClass('active');
//         $('#newsletter').removeClass('active');
//         $('#send-newsletter').removeClass('active');

//     });

//     $('#newsletter').click(function (event) {
//         $('.admin-message').hide()
//         $('.admin-newsletter').show()
//         $('.admin-send-newsletter').hide()
//         $('#messages').removeClass('active');
//         $('#newsletter').addClass('active');
//         $('#send-newsletter').removeClass('active');
//     });

//     $('#send-newsletter').click(function (event) {
//         $('.admin-message').hide()
//         $('.admin-newsletter').hide()
//         $('.admin-send-newsletter').show()
//         $('#newsletter').removeClass('active');
//         $('#messages').removeClass('active');
//         $('#send-newsletter').addClass('active');
//     });
//   });
  

$(document).ready(function () {
    // Function to set active tab in local storage
    function setActiveTab(tabId) {
        localStorage.setItem('activeTab', tabId);
    }

    // Function to get active tab from local storage
    function getActiveTab() {
        return localStorage.getItem('activeTab');
    }

    // Function to show/hide sections based on active tab
    function showActiveSection() {
        var activeTab = getActiveTab();
        if (activeTab === 'newsletter') {
            $('#messages').removeClass('active');
            $('#newsletter').addClass('active');
            $('#send-newsletter').removeClass('active');
            $('.admin-message').hide();
            $('.admin-newsletter').show();
            $('.admin-send-newsletter').hide();
        } else if (activeTab === 'send-newsletter') {
            $('#messages').removeClass('active');
            $('#newsletter').removeClass('active');
            $('#send-newsletter').addClass('active');
            $('.admin-message').hide();
            $('.admin-newsletter').hide();
            $('.admin-send-newsletter').show();
        } else {
            $('#messages').addClass('active');
            $('#newsletter').removeClass('active');
            $('#send-newsletter').removeClass('active');
            $('.admin-message').show();
            $('.admin-newsletter').hide();
            $('.admin-send-newsletter').hide();
        }
    }

    // Set active tab on initial load
    showActiveSection();

    $('#messages').click(function (event) {
        setActiveTab('messages');
        showActiveSection();
    });

    $('#newsletter').click(function (event) {
        setActiveTab('newsletter');
        showActiveSection();
    });

    $('#send-newsletter').click(function (event) {
        setActiveTab('send-newsletter');
        showActiveSection();
    });
});
