var reportApp = angular.module('reportApp',[]);

reportApp.filter('ssnFormat',function() {
    return function(ssn){
        if(ssn == null)
            return '';
        else
            return ssn.slice(0,3) + '-' + ssn.slice(3,5) + '-' + ssn.slice(5);
    };
});

reportApp.filter('awardYearFormat',function() {
    return function(ay){
        if(ay)
            return ay.slice(0,2) + '-' + ay.slice(2);
        else
            return '';
    };
});

reportApp.filter('dateFormat', [
    '$filter', function($filter) {
        return function(input, format) {
            return $filter('date')(new Date(input), format);
        };
    }
]);

reportApp.controller('reportCtrl', function($scope, $http){

    $scope.reports = [];
    $scope.awardYears = [];
    $scope.campuses = [];
    $scope.enrollmentStatuses = [];
    $scope.federalPrograms = [];
    $scope.studyPrograms = [];

    reportHeaders = ['left header','middle header','right header'];
    $scope.gridOptions = {
        columnDefs: [
            { field: 'name' },
            { field: 'gender', visible: false},
            { field: 'company' }
        ],
        enableGridMenu: true,
        exporterMenuVisibleData: false,
        enableSelectAll: true,
        exporterCsvFilename: 'myFile.csv',
        exporterPdfDefaultStyle: {fontSize: 11},
        exporterPdfTableStyle: {margin: [25, 0, 30, 25]},
        exporterPdfTableHeaderStyle: {fontSize: 10, bold: true, italics: true, color: 'red'},
        exporterPdfHeader: function (currentPage, pageCount) {
            return {
                margin: [25,10,25,10],
                table: {
                widths: ['*','*','*'],
                body: [
                    //todo: $scope.schoolName ???
                    [{text: reportHeaders[0], alignment:'left', fontSize:'11'},
                    {text: reportHeaders[1], alignment:'center', fontSize: '16',},
                    {text: reportHeaders[2], alignment:'right', fontSize:'11'}],
                ],
                },
                layout: 'noBorders'
            };
        },
        exporterPdfFooter: function ( currentPage, pageCount ) {
            var now = new Date();
            return { //text: currentPage.toString() + ' of ' + pageCount.toString(), style: 'footerStyle' };
                margin: [25,10,25,0],
                columns: [
                { text: 'Page ' + currentPage.toString() + ' of ' + pageCount.toString(), style: 'footerStyle'},
                { text: now.toLocaleDateString() + ' ' + now.toLocaleTimeString(), alignment: 'right', style: 'footerStyle' }]
            };
        },
        exporterPdfCustomFormatter: function ( docDefinition ) {
            docDefinition.styles.headerStyle = { fontSize: 22, bold: true };
            docDefinition.styles.footerStyle = { fontSize: 10, bold: true };
            docDefinition.content[0].layout = {
                hLineWidth: function(i, node) {return 0;},
                vLineWidth: function(i, node) {return 0;},
            };
            return docDefinition;
        },
        exporterPdfOrientation: 'portrait',
        exporterPdfPageSize: 'LETTER',
        exporterPdfMaxGridWidth: 500,
        exporterCsvLinkElement: angular.element(document.querySelectorAll(".custom-csv-link-location")),
        onRegisterApi: function(gridApi){
        $scope.gridApi = gridApi;
        }
    };

    getAwardYears = function(howMany, blankAtTop, digits2or4){
        var data = { years : howMany, blankItemAtTop: blankAtTop, digits: digits2or4 };
        $http.post('/getawardyears/', data)
            .then(function(response){
            $scope.awardYears = response.data.awardYears;
        });
    }

    getCampuses = function(){
        $http.get('/getcampuses/')
            .then(function(response){
            $scope.campuses = response.data.campuses;

            // push "All" to beginning
            $scope.campuses.unshift({'campusid':0, 'campusname':'All'});
        });
    }

    getEnrollmentStatuses = function(){
        $http.get('/getenrollmentstatuses/')
            .then(function(response){
                $scope.enrollmentStatuses = response.data.enrollmentStatuses;
        });
    }

    getFederalPrograms = function(){
        $http.get('/getfederalprograms/')
            .then(function(response){
            $scope.federalPrograms = response.data.federalPrograms;
        });
    }

    getReports = function(){
        $http.get('/getreports/')
            .then(function(response){
                $scope.reports = response.data.reports;
            })
    }

    getStudyPrograms = function(){
        $http.get('/getstudyprograms/')
            .then(function(response){
            $scope.studyPrograms = response.data.studyPrograms;
        });
    }

    function displayBox(){
        console.log('color box');
        function displayBox(){
            $.colorbox({rel:'group1', transition:'none', width:"90%", height:"95%", html:'<div class="inline" id="inline_content" style="padding:10px; background:#fff;"><h4>Report Viewer</h4></div>'}); // <div ui-grid="gridOptions" ui-grid-selection ui-grid-exporter class="grid"></div></div>'});
        };
            // $.colorbox({rel:'group4', transition:'none', width:"90%", height:"95%", html:'<div class="inline" id="inline_content" style="padding:10px; background:#fff;"><h4>FI Central XML Viewer</h4><div id="processing"></div><pre><code id="xml"></code></pre></div>'});
    
        
    };

    $scope.schools = schools;
    $scope.activeSchool = activeSchool;
    console.log($scope.activeSchool);
    getAwardYears(9, true, 2);
    getCampuses();
    getEnrollmentStatuses();
    getFederalPrograms();
    getReports();
    getStudyPrograms();
    console.log($scope.gridOptions.columnDefs);

    $scope.selectReport = function(report){
        
        $scope.activeReport = report;
        
        // get default campus
        campus = $scope.activeReport.campusdefault ? parseInt($scope.activeReport.campusdefault) : 0;
        var result = $.grep($scope.campuses, function(e){ return e.campusid == campus;});
        if(result.length)
            $scope.activeCampus = result[0];
        else
            $scope.activeCampus = $scope.campuses[0];

        // get date types
        $scope.dateFields = [];
        if(report.datefield1)
            $scope.dateFields.push({'item': 1, 'field': report.datefield1});
        if(report.datefield2)
            $scope.dateFields.push({'item': 2, 'field': report.datefield2});
        if(report.datefield3)
            $scope.dateFields.push({'item': 3, 'field': report.datefield3});
        if(report.datefield4)
            $scope.dateFields.push({'item': 4, 'field': report.datefield4});
        
    };

    $scope.selectCampus = function(campus){
        $scope.activeCampus = campus;
    }

    $scope.selectStatus = function(status){
        var idx = $scope.activeReport.statuses.indexOf(status.enrollmentstatusid)
        if(idx == -1){
            $scope.activeReport.statuses.push(status.enrollmentstatusid);
            $scope.activeReport.statuses.sort(function (a, b) {  return a - b;  });
        }
        else
            $scope.activeReport.statuses.splice(idx,1);
    }

    $scope.allStatuses = function(){
        $scope.activeReport.statuses = [];
        for(i=0; i<$scope.enrollmentStatuses.length; i++){
            $scope.activeReport.statuses.push($scope.enrollmentStatuses[i].enrollmentstatusid);
        }
        $scope.activeReport.statuses.sort(function (a, b) {  return a - b;  });
    }

    $scope.selectFederalProgram = function(pgm){
        var idx = $scope.activeReport.fedpgms.indexOf(pgm.fedpgmid)
        if(idx == -1){
            $scope.activeReport.fedpgms.push(pgm.fedpgmid);
            $scope.activeReport.fedpgms.sort(function (a, b) {  return a - b;  });
        }
        else
            $scope.activeReport.fedpgms.splice(idx,1);
    }

    $scope.allFederalPrograms = function(){
        $scope.activeReport.fedpgms = [];
        for(i=0; i<$scope.federalPrograms.length; i++){
            $scope.activeReport.fedpgms.push($scope.federalPrograms[i].fedpgmid);
        }
        $scope.activeReport.fedpgms.sort(function (a, b) {  return a - b;  });
    }

    $scope.selectStudyProgram = function(pgm){
        var idx = $scope.activeReport.studypgms.indexOf(pgm.programid)
        if(idx == -1){
            $scope.activeReport.studypgms.push(pgm.programid);
            $scope.activeReport.studypgms.sort(function (a, b) {  return a - b;  });
        }
        else
            $scope.activeReport.studypgms.splice(idx,1);
    }

    $scope.allStudyPrograms = function(){
        $scope.activeReport.studypgms = [];
        for(i=0; i<$scope.studyPrograms.length; i++){
            $scope.activeReport.studypgms.push($scope.studyPrograms[i].programid);
        }
        $scope.activeReport.studypgms.sort(function (a, b) {  return a - b;  });
    }

    $scope.generateReport = function(){
        var data = $scope.activeReport;
        data['schoolid'] = $scope.activeSchool.schoolid;
        data['school_id'] = $scope.activeSchool.school_id;
        var result = $.grep($scope.dateFields, function(e){ return e.item == data['datefielddefault'];});
        if(result.length)
            data['datefield'] = result[0]
        $http.post('/generatereport/', data)
            .then(function(response){
                console.log(response.data);
                if(response.data.status == 'error'){
                    $('#message').slideDown(50,'linear',function(){
                        $('#message').html(response.data.msg);
                        $('#message').css('color', '#CC0000');
                    });
                    setTimeout(function(){
                        $('#message').slideUp(100);
                    } , 3000);
                }
                reportHeaders = response.data.headings;
                $scope.gridOptions.columnDefs = response.data.columns;
                $scope.gridOptions.data = response.data.data;
                displayBox();
                // put switch here, set vars for data, orientation, columns
                // pop up colorbox, set its html prop


        });
    }
})