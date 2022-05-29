#include "functions.hpp"
#include "graphs.hpp"

void macro() {
  gStyle->SetOptFit(111111);

  cv = new TCanvas("rawdata", "Raw Data");
  cv->Divide(2, 2);

  cv->cd(1);
  R_pi_raw_graph = new TGraphErrors("../../data/pi/run3-adjusted.csv", "%lg %lg %lg %lg", "  ");
  R_pi_raw_graph->Draw();

  R_pi_raw_fun = new TF1("R_pi_raw_fun", R_pi, 0, 90, 4);
  R_pi_raw_fun->SetParNames("$n_1$", "$n_2$", "$$\\Delta\\theta$$", "$$I_0$$");
  R_pi_raw_fun->SetParameters(1, 1.519, 0, 1000);
  R_pi_raw_fun->SetParLimits(0, 1, 1);
  R_pi_raw_fun->SetParLimits(2, -0.00001, 0.00001);
  R_pi_raw_fun->Draw("same");
  R_pi_raw_graph->Fit(R_pi_raw_fun);

  cv->cd(3);
  ifstream ifs("../../data/pi/run3-adjusted.csv");
  int npoints = 38;
  double x[npoints];
  double y[npoints];
  for (int i = 0; i < npoints; ++i) {
    double _;
    ifs >> x[i] >> y[i] >> _ >> _;
    y[i] -= R_pi_raw_fun->Eval(x[i]);
  }
  auto pi_residual = new TGraph(npoints, x, y);
  pi_residual->Draw();

  // Sigma polarisation ////////////////////////////////////////////////////////
  cv->cd(2);
  R_sigma_raw_graph = new TGraphErrors("../../data/sigma/run1-adjusted.csv", "%lg %lg %lg %lg");
  R_sigma_raw_graph->Draw();

  R_sigma_raw_fun = new TF1("R_sigma_raw_fun", R_sigma, 0, 90, 4);
  R_sigma_raw_fun->SetParNames("$n_1$", "$n_2$", "$$\\Delta\\theta$$", "$$I_0$$");
  R_sigma_raw_fun->SetParameters(1, 1.519, 0, 1000);
  R_sigma_raw_fun->SetParLimits(0, 1, 1);
  R_sigma_raw_fun->SetParLimits(2, -0.00001, 0.00001);
  R_sigma_raw_fun->Draw("same");
  R_sigma_raw_graph->Fit(R_sigma_raw_fun);

  cv->cd(4);
  ifs.close();
  ifs.open("../../data/sigma/run1-adjusted.csv");
  for (int i = 0; i < npoints; ++i) {
    double _;
    ifs >> x[i] >> y[i] >> _ >> _;
    y[i] -= R_sigma_raw_fun->Eval(x[i]);
  }
  auto sigma_resiudal = new TGraph(npoints, x, y);
  sigma_resiudal->Draw();
}




