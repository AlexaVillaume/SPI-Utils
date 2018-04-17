import os
import sys
import numpy as np

def cool_dwarfs(cd, feh, logt, logg):
    log_flux = (cd[1,:] + cd[2,:]*logt + cd[3,:]*feh + cd[4,:]*logg + cd[5,:]*feh*feh +
               cd[6,:]*logt*logt + cd[7,:]*logg*logg + cd[8,:]*logt*feh + cd[9,:]*logt*logg +
               cd[10,:]*feh*logg + cd[11,:]*feh*feh*feh + cd[12,:]*logt*logt*logt +
               cd[13,:]*logg*logg*logg + cd[14,:]*logt*logt*feh + cd[15,:]*logt*feh*feh +
               cd[16,:]*logg*logt*logt + cd[17,:]*logt*logt*logt*logt + cd[18,:]*feh*feh*feh*feh +
               cd[19,:]*logt*logt*feh*feh + cd[20,:]*logt*logt*logt*feh +
               cd[21,:]*logt*logt*logt*logt*logt
                )

    return cd[0,:] * 10**log_flux

def cool_giants(cg, feh, logt, logg):
    log_flux = (cg[1,:] + cg[2,:]*logt + cg[3,:]*feh + cg[4,:]*logg + cg[5,:]*logt*logt +
               cg[6,:]*logg*logg + cg[7,:]*feh*feh + cg[8,:]*feh*logg + cg[9,:]*logt*logg +
               cg[10,:]*logt*feh + cg[11,:]*logt*logt*logt + cg[12,:]*logg*logg*logg +
               cg[13,:]*feh*feh*feh + cg[14,:]*logt*logg*feh + cg[15,:]*logt*logt*feh +
               cg[16,:]*logt*logt*logg + cg[17,:]*feh*feh*logt + cg[18,:]*feh*feh*logg +
               cg[19,:]*logt*logg*logg + cg[20,:]*feh*logg*logg + cg[21,:]*logt*logt*logt*logt
                )

    return cg[0,:] * 10**log_flux

def warm_dwarfs(wd, feh, logt, logg):
    log_flux = (wg[1,:] + wg[2,:]*logt + wg[3,:]*feh + wg[4,:]*logg + wg[5,:]*logt*logt +
               wg[6,:]*logg*logg + wg[7,:]*feh*feh + wg[8,:]*logt*feh + wg[9,:]*logt*logg +
               wg[10,:]*logg*feh + wg[11,:]*logt*logt*logt + wg[12,:]*logg*logg*logg +
               wg[13,:]*feh*feh*feh + wg[14,:]*logt*logt*feh + wg[15,:]*logt*feh*feh +
               wg[16,:]*logg*logt*logt + wg[17,:]*logg*logg*logt + wg[18,:]*logt*logt*logt*logt +
               wg[19,:]*feh*feh*feh*feh + wg[20,:]*logt*logt*feh*feh + wg[21,:]*logt*logt*logg*logg +
               wg[22,:]*feh*feh*logg*logg + wg[23,:]*logt*logt*logt*logt*logt
                )

    return wg[0,:] * 10**log_flux

def warm_dwarfs(wd, feh, logt, logg):
    log_flux = (wd[1,:] + wd[2,:]*logt + wd[3,:]*feh + wd[4,:]*logg + wd[5,:]*logt*logt +
               wd[6,:]*logg*logg + wd[7,:]*feh*feh + wd[8,:]*logt*feh + wd[9,:]*logt*logg +
               wd[10,:]*logt*logt*logt + wd[11,:]*logt*logg*logg + wd[12,:]*feh*feh*feh +
               wd[13,:]*logt*logt*logg + wd[14,:]*logt*logt*feh + wd[15,:]*logt*feh*feh +
               wd[16,:]*logt*logg*feh + wd[17,:]*logg*feh*feh + wd[18,:]*logt*logt*logt*logt +
               wd[19,:]*logg*logg*logg*logg + wd[20,:]*logt*logt*logt*logg +
               wd[21,:]*feh*logt*logt*logt + wd[22,:]*feh*feh*logt*logt +
               wd[23,:]*feh*feh*feh*logt + wd[24,:]*logt*logt*logg*logg +
               wd[25,:]*feh*logt*logt*logg + wd[26,:]*logt*logt*logt*logt*logt
                )

    return wd[0,:] * 10**log_flux

def hot_stars(hs, feh, logt, logg):
    log_flux = (hs[1,:] + hs[2,:]*logt + hs[3,:]*feh + hs[4,:]*logg + hs[5,:]*logt*logt +
               hs[6,:]*feh*feh + hs[7,:]*logg*logg + hs[8,:]*logt*logg + hs[9,:]*logt*feh +
               hs[10,:]*logg*feh + hs[11,:]*logt*logt*logt + hs[12,:]*logg*logg*logg +
               hs[13,:]*feh*feh*feh + hs[14,:]*logt*logg*feh + hs[15,:]*logt*logt*feh +
               hs[16,:]*logt*logt*logg + hs[17,:]*feh*feh*logt + hs[18,:]*feh*feh*logg +
               hs[19,:]*logt*logg*logg + hs[20,:]*feh*logg*logg + hs[21,:]*logt*logt*logt*logt
                )

    return hs[0,:] * 10**log_flux

def from_coefficients(logt, logg, feh):
    """ Generate a stellar spectrum using the
    coeffecients

    Parameters:
    -----------
    logt: float
        log10 of effective temperture
    logg: float
        surface gravity
    feh: float
        metallicity

    Output:
    -------
    flux: ndarray
        interpolated spectrum
    """

    """
    These weights are used later to ensure
    smooth behavior.
    """
    # Overlap of cool dwarf and warm dwarf training sets
    d_teff_overlap = np.linspace(3000, 5500, num=100)
    d_weights = np.linspace(1, 0, num=100)

    # Overlap of warm giant and hot star training sets
    gh_teff_overlap = np.linspace(5500, 6500, num=100)
    gh_weights = np.linspace(1, 0, num=100)

    # Overlap of warm giant and cool giant training sets
    gc_teff_overlap = np.linspace(3500, 4500, num=100)
    gc_weights = np.linspace(1, 0, num=100)

    """
    Open SPI coefficient files
    """
    cd = np.loadtxt('Cool_Dwarfs_coeffs.dat')
    cg = np.loadtxt('Cool_Giants_coeffs.dat')
    wd = np.loadtxt('Warm_Dwarfs_coeffs.dat')
    wg = np.loadtxt('Warm_Giants_coeffs.dat')
    hs = np.loadtxt('Hot_Stars_coeffs.dat')

    cd, cg, wd, wg, hs = cd.T, cg.T, wd.T, wg.T, hs.T

    """
    Setting up some boundaries
    """
    if 10**logt < 2800.:
        logt = np.log10(2800)
    if logg < (-0.5):
        logg = (-0.5)

    # Giants
    if (teff >= 2500. and teff <= 3500. and logg <= 4.0 and logg >= -0.5):
        flux = cool_giants(cg, feh, logt, logg)

    elif (teff >= 4500. and teff <= 5500. and logg <= 4.0 and logg >= -0.5):
        flux = warm_giants(wg, feh, logt, logg)

    elif (teff >= 5500. and teff < 6500. and logg <= 4.0 and logg >= -0.5):
        flux1 = warm_giants(wg, feh, logt, logg)
        flux2 = hot_stars(hs, feh, logt, logg)

        t_index = (np.abs(gh_teff_overlap - teff)).argmin()
        weight = gh_weights[t_index]
        flux = (flux1*weight + flux2*(1-weight))

    elif (teff >= 3500. and teff < 4500. and logg <= 4.0 and logg >= -0.5):
        flux1 = cool_giants(cg, feh, logt, logg)
        flux2 = warm_giants(wg, feh, logt, logg)

        t_index = (np.abs(gc_teff_overlap - teff)).argmin()
        weight = gc_weights[t_index]
        flux = (flux1*weight + flux2*(1-weight))

    # Dwarfs
    elif (teff >= 5500. and teff < 6000. and logg > 4.0):
        flux = warm_dwarfs(wd, feh, logt, logg)

    elif (teff >= 2500. and teff <= 3000. and logg > 4.0):
        flux = cool_dwarfs(cd, feh, logt, logg)

    elif (teff >= 3000. and teff <= 5500. and logg > 4.0):
        flux1 = cool_dwarfs(cd, feh, logt, logg)
        flux2 = warm_dwarfs(wd, feh, logt, logg)

        t_index = (np.abs(d_teff_overlap - teff)).argmin()
        weight = d_weights[t_index]
        flux = (flux1*weight + flux2*(1-weight))

    # Hot stars, have to split this up bcuz of warm stars
    elif (teff >= 6500. and teff <= 12e3 and logg <= 4.0 and logg >= -0.5):
        flux = hot_stars(hs, feh, logt, logg)

    elif (teff >= 6000. and teff <= 12e3 and logg > 4.0):
        flux = hot_stars(hs, feh, logt, logg)
    else:
        error = ('Parameter out of bounds:'
                 'teff = {0},  logg {1}')
        raise ValueError(error.format(teff, logg))

    return flux

if __name__=='__main__':
    pass
