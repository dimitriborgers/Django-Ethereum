#import files required for django set-up
from django.shortcuts import render
from hasher.forms import RetreiveHostAddr
from django.views.generic import TemplateView
from django.views import View

#import files required for Ethereum node access
from web3 import Web3,HTTPProvider
from hasher.algorithm import find_hashes

class ContractView(View):
    #get method renders an html page with a form
    def get(self,request):
        form = RetreiveHostAddr()
        return render(request, 'hasher/home.html', {'form':form})

    #post method sends back inputted form to server and re-renders a page
    def post(self, request):
        #request.POST refills form with data recieved from request
        form = RetreiveHostAddr(request.POST)

        #clean-up data
        if form.is_valid():
            host = form.cleaned_data['hostForm']
            host = 'https://mainnet.infura.io/'+host
            addr = form.cleaned_data['addrForm']
            result_hash, block_hash, block_transactions = find_hashes(addr,host)

            #Re-enitialize form so that input box is empty
            form = RetreiveHostAddr()
            return render(request, 'hasher/home.html', {'form':form,'host':host,'addr':addr,'result_hash':result_hash,'block_hash':block_hash, 'block_transactions':block_transactions})
