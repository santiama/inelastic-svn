// Copyright 2006-2007 Brandon Keith.  See LICENSE file for details. 
#include "TabPe.h"

static tabPe instance;

tabPe *periodicTable(void)
{
    return &instance;
}


tabPe::tabPe ()
{
    simbolo = new String[104];
    sz = new double[104];
    en1 = new double[104];
    en2 = new double[104];
    en3 = new double[104];
    simbolo[0] = "x ";
    sz[0] = 0.50;
    en1[0] = 0.30;
    en2[0] = 0.30;
    en3[0] = 0.30;
    simbolo[1] = "h ";
    sz[1] = 1.10;
    en1[1] = 0.32;
    en2[1] = 0.30;
    en3[1] = 0.30;
    simbolo[2] = "he";
    sz[2] = 2.20;
    en1[2] = 1.60;
    en2[2] = 0.90;
    en3[2] = 0.90;
    simbolo[3] = "li";
    sz[3] = 1.22;
    en1[3] = 0.68;
    en2[3] = 1.10;
    en3[3] = 1.10;
    simbolo[4] = "be";
    sz[4] = 0.63;
    en1[4] = 0.35;
    en2[4] = 0.85;
    en3[4] = 0.80;
    simbolo[5] = "b ";
    sz[5] = 1.55;
    en1[5] = 0.82;
    en2[5] = 0.85;
    en3[5] = 0.85;
    simbolo[6] = "c ";
    sz[6] = 1.55;
    en1[6] = 0.68;
    en2[6] = 0.65;
    en3[6] = 0.60;
    simbolo[7] = "n ";
    sz[7] = 1.40;
    en1[7] = 0.75;
    en2[7] = 0.60;
    en3[7] = 0.60;
    simbolo[8] = "o ";
    sz[8] = 1.35;
    en1[8] = 0.73;
    en2[8] = 0.55;
    en3[8] = 0.55;
    simbolo[9] = "f ";
    sz[9] = 1.30;
    en1[9] = 0.72;
    en2[9] = 0.65;
    en3[9] = 0.65;
    simbolo[10] = "ne";
    sz[10] = 2.02;
    en1[10] = 1.12;
    en2[10] = 0.65;
    en3[10] = 0.65;
    simbolo[11] = "na";
    sz[11] = 2.20;
    en1[11] = 0.97;
    en2[11] = 1.50;
    en3[11] = 1.50;
    simbolo[12] = "mg";
    sz[12] = 1.50;
    en1[12] = 1.10;
    en2[12] = 1.35;
    en3[12] = 1.35;
    simbolo[13] = "al";
    sz[13] = 1.50;
    en1[13] = 1.35;
    en2[13] = 1.15;
    en3[13] = 1.15;
    simbolo[14] = "si";
    sz[14] = 2.20;
    en1[14] = 1.20;
    en2[14] = 0.60;
    en3[14] = 0.60;
    simbolo[15] = "p ";
    sz[15] = 1.88;
    en1[15] = 1.05;
    en2[15] = 0.90;
    en3[15] = 0.80;
    simbolo[16] = "s ";
    sz[16] = 1.81;
    en1[16] = 1.02;
    en2[16] = 0.90;
    en3[16] = 0.90;
    simbolo[17] = "cl";
    sz[17] = 1.75;
    en1[17] = 0.99;
    en2[17] = 0.90;
    en3[17] = 0.90;
    simbolo[18] = "ar";
    sz[18] = 2.77;
    en1[18] = 1.57;
    en2[18] = 0.95;
    en3[18] = 0.95;
    simbolo[19] = "k ";
    sz[19] = 2.39;
    en1[19] = 1.33;
    en2[19] = 2.30;
    en3[19] = 2.30;
    simbolo[20] = "ca";
    sz[20] = 1.95;
    en1[20] = 0.99;
    en2[20] = 1.70;
    en3[20] = 1.70;
    simbolo[21] = "sc";
    sz[21] = 1.32;
    en1[21] = 1.44;
    en2[21] = 1.40;
    en3[21] = 1.40;
    simbolo[22] = "ti";
    sz[22] = 1.95;
    en1[22] = 1.47;
    en2[22] = 1.30;
    en3[22] = 1.30;
    simbolo[23] = "v ";
    sz[23] = 1.06;
    en1[23] = 1.33;
    en2[23] = 1.20;
    en3[23] = 1.20;
    simbolo[24] = "cr";
    sz[24] = 1.13;
    en1[24] = 1.35;
    en2[24] = 1.10;
    en3[24] = 1.10;
    simbolo[25] = "mn";
    sz[25] = 1.19;
    en1[25] = 1.35;
    en2[25] = 1.10;
    en3[25] = 1.10;
    simbolo[26] = "fe";
    sz[26] = 1.95;
    en1[26] = 1.34;
    en2[26] = 1.10;
    en3[26] = 1.10;
    simbolo[27] = "co";
    sz[27] = 1.13;
    en1[27] = 1.33;
    en2[27] = 1.10;
    en3[27] = 1.10;
    simbolo[28] = "ni";
    sz[28] = 1.24;
    en1[28] = 1.50;
    en2[28] = 1.10;
    en3[28] = 1.10;
    simbolo[29] = "cu";
    sz[29] = 1.15;
    en1[29] = 1.52;
    en2[29] = 1.10;
    en3[29] = 1.10;
    simbolo[30] = "zn";
    sz[30] = 1.15;
    en1[30] = 1.45;
    en2[30] = 1.10;
    en3[30] = 1.10;
    simbolo[31] = "ga";
    sz[31] = 1.55;
    en1[31] = 1.22;
    en2[31] = 0.60;
    en3[31] = 0.60;
    simbolo[32] = "ge";
    sz[32] = 4.00;
    en1[32] = 1.17;
    en2[32] = 0.60;
    en3[32] = 0.60;
    simbolo[33] = "as";
    sz[33] = 0.83;
    en1[33] = 1.21;
    en2[33] = 0.60;
    en3[33] = 0.60;
    simbolo[34] = "se";
    sz[34] = 0.90;
    en1[34] = 1.22;
    en2[34] = 0.60;
    en3[34] = 0.60;
    simbolo[35] = "br";
    sz[35] = 1.75;
    en1[35] = 1.21;
    en2[35] = 0.60;
    en3[35] = 0.60;
    simbolo[36] = "kr";
    sz[36] = 1.90;
    en1[36] = 1.60;
    en2[36] = 0.60;
    en3[36] = 0.60;
    simbolo[37] = "rb";
    sz[37] = 2.65;
    en1[37] = 1.47;
    en2[37] = 0.60;
    en3[37] = 0.60;
    simbolo[38] = "sr";
    sz[38] = 2.02;
    en1[38] = 1.12;
    en2[38] = 0.60;
    en3[38] = 0.60;
    simbolo[39] = "y ";
    sz[39] = 1.61;
    en1[39] = 1.78;
    en2[39] = 0.60;
    en3[39] = 0.60;
    simbolo[40] = "zr";
    sz[40] = 1.42;
    en1[40] = 1.56;
    en2[40] = 0.60;
    en3[40] = 0.60;
    simbolo[41] = "nb";
    sz[41] = 1.33;
    en1[41] = 1.48;
    en2[41] = 0.60;
    en3[41] = 0.60;
    simbolo[42] = "mo";
    sz[42] = 1.75;
    en1[42] = 1.47;
    en2[42] = 0.60;
    en3[42] = 0.60;
    simbolo[43] = "tc";
    sz[43] = 1.80;
    en1[43] = 1.35;
    en2[43] = 0.60;
    en3[43] = 0.60;
    simbolo[44] = "ru";
    sz[44] = 1.20;
    en1[44] = 1.40;
    en2[44] = 0.60;
    en3[44] = 0.60;
    simbolo[45] = "rh";
    sz[45] = 1.22;
    en1[45] = 1.45;
    en2[45] = 0.60;
    en3[45] = 0.60;
    simbolo[46] = "pd";
    sz[46] = 1.44;
    en1[46] = 1.50;
    en2[46] = 0.60;
    en3[46] = 0.60;
    simbolo[47] = "ag";
    sz[47] = 1.55;
    en1[47] = 1.59;
    en2[47] = 0.60;
    en3[47] = 0.60;
    simbolo[48] = "cd";
    sz[48] = 1.75;
    en1[48] = 1.69;
    en2[48] = 0.60;
    en3[48] = 0.60;
    simbolo[49] = "in";
    sz[49] = 1.45;
    en1[49] = 1.63;
    en2[49] = 0.60;
    en3[49] = 0.60;
    simbolo[50] = "sn";
    sz[50] = 1.67;
    en1[50] = 1.46;
    en2[50] = 0.60;
    en3[50] = 0.60;
    simbolo[51] = "sb";
    sz[51] = 1.12;
    en1[51] = 0.62;
    en2[51] = 0.60;
    en3[51] = 0.60;
    simbolo[52] = "te";
    sz[52] = 1.26;
    en1[52] = 0.70;
    en2[52] = 0.60;
    en3[52] = 0.60;
    simbolo[53] = "i ";
    sz[53] = 1.75;
    en1[53] = 1.40;
    en2[53] = 0.60;
    en3[53] = 0.60;
    simbolo[54] = "xe";
    sz[54] = 2.10;
    en1[54] = 1.70;
    en2[54] = 0.60;
    en3[54] = 0.60;
    simbolo[55] = "cs";
    sz[55] = 3.01;
    en1[55] = 1.67;
    en2[55] = 0.60;
    en3[55] = 0.60;
    simbolo[56] = "ba";
    sz[56] = 2.41;
    en1[56] = 1.34;
    en2[56] = 0.60;
    en3[56] = 0.60;
    simbolo[57] = "la";
    sz[57] = 1.83;
    en1[57] = 1.02;
    en2[57] = 0.60;
    en3[57] = 0.60;
    simbolo[58] = "ce";
    sz[58] = 1.86;
    en1[58] = 1.03;
    en2[58] = 0.60;
    en3[58] = 0.60;
    simbolo[59] = "pr";
    sz[59] = 1.62;
    en1[59] = 0.90;
    en2[59] = 0.60;
    en3[59] = 0.60;
    simbolo[60] = "nd";
    sz[60] = 1.79;
    en1[60] = 0.99;
    en2[60] = 0.60;
    en3[60] = 0.60;
    simbolo[61] = "pm";
    sz[61] = 1.76;
    en1[61] = 0.98;
    en2[61] = 0.60;
    en3[61] = 0.60;
    simbolo[62] = "sm";
    sz[62] = 1.74;
    en1[62] = 0.96;
    en2[62] = 0.60;
    en3[62] = 0.60;
    simbolo[63] = "eu";
    sz[63] = 1.96;
    en1[63] = 1.09;
    en2[63] = 0.60;
    en3[63] = 0.60;
    simbolo[64] = "gd";
    sz[64] = 1.69;
    en1[64] = 0.94;
    en2[64] = 0.60;
    en3[64] = 0.60;
    simbolo[65] = "tb";
    sz[65] = 1.66;
    en1[65] = 0.92;
    en2[65] = 0.60;
    en3[65] = 0.60;
    simbolo[66] = "dy";
    sz[66] = 1.63;
    en1[66] = 0.91;
    en2[66] = 0.60;
    en3[66] = 0.60;
    simbolo[67] = "ho";
    sz[67] = 1.61;
    en1[67] = 1.89;
    en2[67] = 0.60;
    en3[67] = 0.60;
    simbolo[68] = "er";
    sz[68] = 1.59;
    en1[68] = 1.88;
    en2[68] = 0.60;
    en3[68] = 0.60;
    simbolo[69] = "tm";
    sz[69] = 1.57;
    en1[69] = 1.87;
    en2[69] = 0.60;
    en3[69] = 0.60;
    simbolo[70] = "yb";
    sz[70] = 1.54;
    en1[70] = 1.86;
    en2[70] = 0.60;
    en3[70] = 0.60;
    simbolo[71] = "lu";
    sz[71] = 1.53;
    en1[71] = 1.85;
    en2[71] = 0.60;
    en3[71] = 0.60;
    simbolo[72] = "hf";
    sz[72] = 1.40;
    en1[72] = 1.78;
    en2[72] = 0.60;
    en3[72] = 0.60;
    simbolo[73] = "ta";
    sz[73] = 1.22;
    en1[73] = 1.68;
    en2[73] = 0.60;
    en3[73] = 0.60;
    simbolo[74] = "w ";
    sz[74] = 1.26;
    en1[74] = 1.70;
    en2[74] = 0.60;
    en3[74] = 0.60;
    simbolo[75] = "re";
    sz[75] = 1.30;
    en1[75] = 1.72;
    en2[75] = 0.60;
    en3[75] = 0.60;
    simbolo[76] = "os";
    sz[76] = 1.58;
    en1[76] = 1.88;
    en2[76] = 0.60;
    en3[76] = 0.60;
    simbolo[77] = "ir";
    sz[77] = 1.22;
    en1[77] = 1.68;
    en2[77] = 0.60;
    en3[77] = 0.60;
    simbolo[78] = "pt";
    sz[78] = 1.55;
    en1[78] = 1.30;
    en2[78] = 0.60;
    en3[78] = 0.60;
    simbolo[79] = "au";
    sz[79] = 1.45;
    en1[79] = 1.34;
    en2[79] = 0.60;
    en3[79] = 0.60;
    simbolo[80] = "hg";
    sz[80] = 1.98;
    en1[80] = 1.10;
    en2[80] = 0.60;
    en3[80] = 0.60;
    simbolo[81] = "tl";
    sz[81] = 1.71;
    en1[81] = 0.95;
    en2[81] = 0.60;
    en3[81] = 0.60;
    simbolo[82] = "pb";
    sz[82] = 2.16;
    en1[82] = 1.20;
    en2[82] = 0.60;
    en3[82] = 0.60;
    simbolo[83] = "bi";
    sz[83] = 1.73;
    en1[83] = 0.96;
    en2[83] = 0.60;
    en3[83] = 0.60;
    simbolo[84] = "po";
    sz[84] = 1.21;
    en1[84] = 0.67;
    en2[84] = 0.60;
    en3[84] = 0.60;
    simbolo[85] = "at";
    sz[85] = 1.12;
    en1[85] = 0.62;
    en2[85] = 0.60;
    en3[85] = 0.60;
    simbolo[86] = "rn";
    sz[86] = 2.30;
    en1[86] = 1.90;
    en2[86] = 0.60;
    en3[86] = 0.60;
    simbolo[87] = "fr";
    sz[87] = 3.24;
    en1[87] = 1.80;
    en2[87] = 0.60;
    en3[87] = 0.60;
    simbolo[88] = "ra";
    sz[88] = 2.57;
    en1[88] = 1.43;
    en2[88] = 0.60;
    en3[88] = 0.60;
    simbolo[89] = "ac";
    sz[89] = 2.12;
    en1[89] = 1.18;
    en2[89] = 0.60;
    en3[89] = 0.60;
    simbolo[90] = "th";
    sz[90] = 1.84;
    en1[90] = 1.02;
    en2[90] = 0.60;
    en3[90] = 0.60;
    simbolo[91] = "pa";
    sz[91] = 1.60;
    en1[91] = 0.89;
    en2[91] = 0.60;
    en3[91] = 0.60;
    simbolo[92] = "u ";
    sz[92] = 1.75;
    en1[92] = 0.97;
    en2[92] = 0.60;
    en3[92] = 0.60;
    simbolo[93] = "np";
    sz[93] = 1.71;
    en1[93] = 0.95;
    en2[93] = 0.60;
    en3[93] = 0.60;
    simbolo[94] = "pu";
    sz[94] = 1.67;
    en1[94] = 0.93;
    en2[94] = 0.60;
    en3[94] = 0.60;
    simbolo[95] = "am";
    sz[95] = 1.66;
    en1[95] = 0.92;
    en2[95] = 0.60;
    en3[95] = 0.60;
    simbolo[96] = "cm";
    sz[96] = 1.65;
    en1[96] = 0.91;
    en2[96] = 0.60;
    en3[96] = 0.60;
    simbolo[97] = "bk";
    sz[97] = 1.64;
    en1[97] = 0.90;
    en2[97] = 0.60;
    en3[97] = 0.60;
    simbolo[98] = "cf";
    sz[98] = 1.63;
    en1[98] = 0.89;
    en2[98] = 0.60;
    en3[98] = 0.60;
    simbolo[99] = "es";
    sz[99] = 1.62;
    en1[99] = 0.88;
    en2[99] = 0.60;
    en3[99] = 0.60;
    simbolo[100] = "fm";
    sz[100] = 1.61;
    en1[100] = 0.87;
    en2[100] = 0.60;
    en3[100] = 0.60;
    simbolo[101] = "md";
    sz[101] = 1.60;
    en1[101] = 0.86;
    en2[101] = 0.60;
    en3[101] = 0.60;
    simbolo[102] = "no";
    sz[102] = 1.59;
    en1[102] = 0.85;
    en2[102] = 0.60;
    en3[102] = 0.60;
    simbolo[103] = "lw";
    sz[103] = 1.58;
    en1[103] = 0.84;
    en2[103] = 0.60;
    en3[103] = 0.60;
}

String tabPe::getSimbolo (int i)
{
    return simbolo[i];
}

double tabPe::getSize (int i)
{
    return sz[i];
}