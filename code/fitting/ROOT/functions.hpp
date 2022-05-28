#ifndef FUNCTIONS_HPP
#define FUNCTIONS_HPP

inline TCanvas* cv;
inline TF1* r_pi_fun;
inline TF1* r_sigma_fun;
inline TF1* R_pi_fun;
inline TF1* R_sigma_fun;
inline TF1* R_pi_raw_fun;
inline TF1* R_sigma_raw_fun;

// Ampiezza riflessa con polarizzazione pi
inline double r_pi(double *xx,double *par) {
  const double n1         =  par[0];
  const double n2         =  par[1];
  const double deltaTheta =  par[2];

  const double theta1 = (xx[0] - deltaTheta) / 180 * TMath::Pi();

  const double theta2 = TMath::ASin(n1 / n2 * TMath::Sin(theta1));

  return (n1 * cos(theta2) - n2 * cos(theta1)) / (n1 * cos(theta2) + n2 * cos(theta1));
}

// Ampiezza riflessa con polarizzazione sigma
inline double r_sigma(double *xx,double *par) {
  const double n1         =  par[0];
  const double n2         =  par[1];
  const double deltaTheta =  par[2];

  const double theta1 = (xx[0] - deltaTheta) / 180 * TMath::Pi();

  const double theta2 = TMath::ASin(n1 / n2 * TMath::Sin(theta1));

  return (n1 * cos(theta1) - n2 * cos(theta2)) / (n1 * cos(theta1) + n2 * cos(theta2));
}

// Intensità riflessa con polarizzazione pi
inline double R_pi(double *xx,double *par) {
  const double I_0 = par[3];

  return I_0 * pow(r_pi(xx, par), 2);
}

// Ampiezza riflessa con polarizzazione sigma
inline double R_sigma(double *xx,double *par) {
  const double I_0 = par[3];

  return I_0 * pow(r_sigma(xx, par), 2);
}

//double T_p2(double *xx,double *par) {
//  return 1 - R_p2(xx, par);
//}
//
//double T_s2(double *xx,double *par) {
//  return 1 - R_s2(xx, par);

#endif // define FUNCTIONS_HPP
