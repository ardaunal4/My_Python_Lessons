void pseudorapidity(){
	double theta, eta;
	cout<<"Enter angle theta value : ";
	cin>>theta;
	cout<<endl;
	eta = - log(tan(theta/2));
	cout<<"eta = "<<eta<<endl;
}
