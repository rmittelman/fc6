var fcApp = angular.module('fcApp',[]);

fcApp.filter('ssnFormat',function() {
    return function(ssn){
        if(ssn == null)
            return '';
        else
            return ssn.slice(0,3) + '-' + ssn.slice(3,5) + '-' + ssn.slice(5);
    };
});

fcApp.filter('awardYearFormat',function() {
    return function(ay){
        if(ay)
            return ay.slice(0,2) + '-' + ay.slice(2);
        else
            return '';
    };
});

fcApp.filter('dateFormat', [
    '$filter', function($filter) {
        return function(input, format) {
            return $filter('date')(new Date(input), format);
        };
    }
]);

fcApp.filter('studentFilter', function() {
    return function(item) {
        if(item.lastname.includes($scope.student_search))
            return true;
        else
            return false;
    };
});

fcApp.controller('fcCtrl', function($scope, $http){
    
    $scope.students = [];
    $scope.profiles = [];
    $scope.fundings = [];
    $scope.payments = [];
    $scope.awardYears = [];
    $scope.activeStudent = {};
    $scope.pristineStudent = {};
    $scope.activeProfile = {};
    $scope.tab_1_active = true;
    $scope.tab_2_active = false;
    $scope.tab_3_active = false;
    $scope.tab_4_active = false;
    $scope.message = '';

    // setup lists
    $scope.housingTypes = [
        { id: 1, name: "On Campus" },
        { id: 2, name: "With Parent" },
        { id: 3, name: "Off Campus" },
    ]

    $scope.isirModels = [
        { id: 'D', name: "Dependent" },
        { id: 'I', name: "Independent" },
    ]

    getAwardYears = function(howMany, blankAtTop, digits2or4){
        var data = { years : howMany, blankItemAtTop: blankAtTop, digits: digits2or4 };
        $http.post('/getawardyears/', data)
            .then(function(response){
            $scope.awardYears = response.data.awardYears;
        });
    }

    getYears = function(howMany){
        var today = new Date();
        var yr = today.getFullYear();
        var yr1 = parseInt(yr + 1);
        $scope.needYears = [];
        for(i = 0; i < howMany; i++){
            strYear = (yr1-i).toString();
            $scope.needYears.push(strYear);
        }
    }

    getCampuses = function(){
        $http.get('/getcampuses/')
            .then(function(response){
            $scope.campuses = response.data.campuses;
        });
    }

    getCheckTos = function(){
        $http.get('/getchecktos/')
            .then(function(response){
            $scope.checkTos = response.data.checkTos;
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

    getIsirIrsTypes = function(){
        $http.get('/getisirirstypes/')
            .then(function(response){
            $scope.isirIrsTypes = response.data.isirIrsTypes;
        });
    }

    getIsirVerifyTypes = function(){
        $http.get('/getisirverifytypes/')
            .then(function(response){
            $scope.isirVerifyTypes = response.data.isirVerifyTypes;
        });
    }
    
    $scope.getStudents = function(){
        $http.get('/getstudents/')
            .then(function(response){
                $scope.students = response.data.students;
        });
    };

    $scope.submitStudentForm = function(isValid){
        
        $http.post('/setstudent/update/', $scope.activeStudent)
            .then(function(response){
                $scope.studentForm.$setUntouched();
                $scope.studentForm.$setPristine();
                // $('#message').css('color', '#CC0000');
                // $('#message').html('Student updated.');
                $('#message').slideDown(50,'linear',function(){
                    $('#message').html('Student updated.');
                    $('#message').css('color', '#CC0000');
                });
                // setTimeout("$('#message').fadeOut(); $scope.studentForm.$setPristine(true);", 3000);
                setTimeout(function(){
                    $('#message').slideUp(100);
                } , 2000);


                //$scope.message = 'Student Updated';
                //setTimeout(function(){$scope.message="";}, 2000);
                // console.log(response.data);
            })
                
            .catch(function(response){
            });

    }
    
    // called when user types in find box
    $scope.selectFirstStudent = function(event){
        if(event.keyCode == 13) {
            $scope.selectStudent($scope.filtered[0]);
        }
    }
    
    // provide description of isir model
    $scope.isirModelDescription = function(){
        if($scope.activeProfile.isir_model){
            var result = $.grep($scope.isirModels, function(e){ return e.id == $scope.activeProfile.isir_model; });
            if(result.length)
                return result[0].name;
            else
                return null;
        }
        else
            return null;
    }

    // models for calculated fields
    $scope.calcFees = function(){
        var fees = 
            (parseFloat($scope.activeProfile.tuitionfee) || 0) +
            (parseFloat($scope.activeProfile.registrationfee) || 0) +
            (parseFloat($scope.activeProfile.booksfee) || 0) +
            (parseFloat($scope.activeProfile.strffee) || 0) +
            (parseFloat($scope.activeProfile.otherfee1) || 0) +
            (parseFloat($scope.activeProfile.otherfee2) || 0);
            // if(isNaN(fees))
            //     fees = 0;
            return fees.toFixed(2);
    }

    $scope.calcAllowances = function(){
        var allowances = 
            (parseFloat($scope.activeProfile.foodhousingexp) || 0) +
            (parseFloat($scope.activeProfile.transportationexp) || 0) +
            (parseFloat($scope.activeProfile.personalexp) || 0) +
            (parseFloat($scope.activeProfile.childcareexp) || 0) +
            (parseFloat($scope.activeProfile.otherexp) || 0);
            // if(isNaN(allowances))
            //     allowances = 0;
            return allowances.toFixed(2);
    }
    
    $scope.calcAwards = function(){
        var ttlAwards = 0.00;
        for(i=0; i<$scope.fundings.length; i++){
            ttlAwards += (parseFloat($scope.fundings[i].fundingamount) || 0);
        }
        return ttlAwards.toFixed(2);
    }

    $scope.calcLoanFees = function(){
        var ttlFees = 0.00;
        for(i=0; i<$scope.fundings.length; i++){
            ttlFees += (parseFloat($scope.fundings[i].fundingamount || 0) * (parseFloat($scope.fundings[i].loanfee) || 0));
        }
        return ttlFees.toFixed(2);
    }

    $scope.calcCoa = function(){
        var coa = 
            parseFloat($scope.calcBudget()) +
            parseFloat($scope.calcLoanFees());
        return coa;
    }

    $scope.calcRemainingNeed = function(){
        var rem =
            parseFloat($scope.calcCoa()) -
            (parseFloat($scope.activeProfile.efc_used) || 0);
        return rem;
    }

    $scope.calcFaWithoutDl = function(){
        var fa = 0.00;
        for(i=0; i<$scope.fundings.length; i++){
            
            var funding = $scope.fundings[i];
            //if(funding.studentprofileid == $scope.activeProfile.studentprofileid){
                var fpgms = $.grep($scope.federalPrograms, function(e){ return e.fedpgmid == funding.fedpgmid; });
                if(fpgms.length){
                    var fpgm = fpgms[0];
                    if(fpgm.fawostafford)
                        fa += (parseFloat($scope.fundings[i].fundingamount) || 0);
                }
            //}
        }
        return fa;
    }

    $scope.calcFaWithDl = function(){
        var fa = 0.00;
        for(i=0; i<$scope.fundings.length; i++){
            
            var funding = $scope.fundings[i];
            //if(funding.studentprofileid == $scope.activeProfile.studentprofileid){
                var fpgms = $.grep($scope.federalPrograms, function(e){ return e.fedpgmid == funding.fedpgmid; });
                if(fpgms.length){
                    var fpgm = fpgms[0];
                    if(fpgm.fawstafford)
                        fa += (parseFloat($scope.fundings[i].fundingamount) || 0);
                }
            //}
        }
        return fa;
    }

    $scope.calcNeedForDl = function(){
        var amt = 
            parseFloat($scope.calcRemainingNeed()) - 
            parseFloat($scope.calcFaWithoutDl());
            return amt;

    }

    $scope.calcNeedForOther = function(){
        var amt = 
            parseFloat($scope.calcRemainingNeed()) - 
            parseFloat($scope.calcFaWithDl());
            return amt;

    }

    $scope.calcMonths = function(){
        return Math.round(($scope.activeProfile.programweeks || 0) / 4.33);
    }

    $scope.calcYearlyAllowance = function(){
        var ya = parseFloat($scope.calcAllowances()) * parseFloat($scope.calcMonths());
        if(isNaN(ya))
            ya = 0;
        return ya.toFixed(2);
    }

    $scope.calcBudget = function(){
        var ya = parseFloat($scope.calcYearlyAllowance());
        var tf = parseFloat($scope.calcFees());
        var tb = ya + tf;
        return tb.toFixed(2);
    }

    // for highlighting selected tab
    $scope.switchTab = function(tabNo){
        $scope.tab_1_active = (tabNo == 1);
        $scope.tab_2_active = (tabNo == 2);
        $scope.tab_3_active = (tabNo == 3);
        $scope.tab_4_active = (tabNo == 4);
    }

    // call these when page loads.
    //getAwardYears(9, false, 2);
    $scope.awardYears = awardYears;
    $scope.activeYear = activeYear;
    getYears(10);
    getCampuses();
    getCheckTos();
    getEnrollmentStatuses();
    getFederalPrograms();
    getIsirIrsTypes();
    getIsirVerifyTypes();
    $scope.getStudents();
    
    // for evaluating whether submit button is available
    $scope.okToSubmit = function(){

        var isOk = true;
        //isOk = isOk && $scope.activeStudent.address2 != $scope.pristineStudent.address2;
        //isOk = isOk && ! (json.stringify($scope.activeStudent) === json.stringify($scope.pristineStudent));

        return isOk;
    };

    $scope.selectStudent = function(student){
        $http.get('/getstudentdata/' + student.studentid + '/').then(
            function(response) {
                $scope.activeProfile = {};
                if(response.data.status == 'error') {
                    $scope.profiles = [];
                    $scope.fundings = [];
                    $scope.payments = [];
                    alert(response.data.msg);
                }
                else {
                    $scope.profiles = response.data.profiles;
                    $scope.fundings = response.data.fundings;
                    $scope.payments = response.data.payments;
                    $scope.activeStudent = student;
                    $scope.pristineStudent = angular.copy($scope.activeStudent);
                    $scope.student_search = "";
                }
            }
        );
    };

    $scope.selectProfile = function(profile){
        $scope.activeProfile = profile;
    };

    $scope.selectFunding = function(funding){
        $scope.activeFunding = funding;
    };

    $scope.selectPayment = function(payment){
        $scope.activePayment = payment;
    };

})