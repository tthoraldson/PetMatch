import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import IconButton from '@mui/material/IconButton';
import MenuIcon from '@mui/icons-material/Menu';
import AccountCircle from '@mui/icons-material/AccountCircle';
import MenuItem from '@mui/material/MenuItem';
import Menu from '@mui/material/Menu';
import { useAuth0 } from '@auth0/auth0-react';
import { useNavigate } from "react-router-dom";
import { useState } from 'react';
import { Drawer, ListItem, ListItemIcon, ListItemText } from '@mui/material';
import LoyaltyIcon from '@mui/icons-material/Loyalty';
import HomeIcon from '@mui/icons-material/Home';
import InfoIcon from '@mui/icons-material/Info';
import InsertCommentIcon from '@mui/icons-material/InsertComment';
import SettingsSuggestIcon from '@mui/icons-material/SettingsSuggest';

export default function MenuAppBar() {
  const { user } = useAuth0();
  const navigate = useNavigate();
  const { logout } = useAuth0();
  const [anchorEl, setAnchorEl] = React.useState(null);
  const [open, setOpen] = useState(false);

  const publicRoutes = [
    {
      name: "Home",
      icon: <HomeIcon />,
    },
    {
      name: "About",
      icon: <InfoIcon />,
    },
    {
      name: "Feeback",
      icon: <InsertCommentIcon />,
    },
    ];

    const protectedRoutes = [
      {
        name: "Home",
        icon: <HomeIcon />,
      },
      {
        name: "Matches",
        icon: <LoyaltyIcon />,
      },
      {
        name: "Preferences",
        icon: <SettingsSuggestIcon />,
      },
      {
        name: "About",
        icon: <InfoIcon />,
      },
      {
        name: "Feeback",
        icon: <InsertCommentIcon />,
      },
    ]
    
  const handleMenu = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };

  const goToPreferences = () => {
    navigate('/preferences');
  }

  const goToHome = () => {
    navigate('/home');
  }

  const getList = () => {
    const data = user ? protectedRoutes : publicRoutes;
    
    return (
    <div style={{ width: 250 }} onClick={() => setOpen(false)}>
    {data.map((item, index) => (
        <ListItem button key={index}>
        <ListItemIcon>{item.icon}</ListItemIcon>
        <ListItemText primary={item.name} />
        </ListItem>
    ))}
    </div>
)};

  const logoutButton = () => {
    logout({ logoutParams: { returnTo: window.location.origin } });
  }

  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position="static">
        <Toolbar>
          <IconButton
            size="large"
            edge="start"
            color="inherit"
            aria-label="menu"
            sx={{ mr: 2 }}
            onClick={() => setOpen(true)}
          >
            <MenuIcon />
          </IconButton>
          <Drawer open={open} anchor={"left"} onClose={() => setOpen(false)}>
            {getList()}
          </Drawer>
            <Typography variant="h6" component="div" sx={{ flexGrow: 1, '&:hover': {color: "lightgray", cursor: "default"} }} onClick={goToHome}>
              PetMatch 🐶
            </Typography>
          {user && (
            <div>
              <IconButton
                size="large"
                aria-label="account of current user"
                aria-controls="menu-appbar"
                aria-haspopup="true"
                onClick={handleMenu}
                color="inherit"
              >
                <AccountCircle />
              </IconButton>
              <Menu
                id="menu-appbar"
                anchorEl={anchorEl}
                anchorOrigin={{
                  vertical: 'top',
                  horizontal: 'right',
                }}
                keepMounted
                transformOrigin={{
                  vertical: 'top',
                  horizontal: 'right',
                }}
                open={Boolean(anchorEl)}
                onClose={handleClose}
              >
                <MenuItem onClick={() => {
                  goToPreferences();
                  handleClose();
                }}>Profile</MenuItem>
                <MenuItem onClick={() => {
                  handleClose();
                  logoutButton();
                  }}>Logout</MenuItem>
              </Menu>
            </div>
          )}
        </Toolbar>
      </AppBar>
    </Box>
  );
}
