{
    TCanvas *cv = new TCanvas();
    TFile *rf = new TFile("data.root", "NEW") //root dosyası oluşturuyoruz
    ifstream data; //data adında bir class oluşturuyoruz
    data.open("data.txt");
    int c; //metin dosyasından okunan verileri atamak için oluşturulan değişken
    TH1I *histo = new TH1I("h", "Example", 15, 0, 15);
    while( !(data >> c) == 0){
        //cout<<c<<endl;
        histo -> Fill(c);
    }

    histo -> Draw();
    cv -> Print("data.pdf");
    data.close();
    rf -> Write(); //dosyaya içeriği yazar
    rf -> Close();
}
