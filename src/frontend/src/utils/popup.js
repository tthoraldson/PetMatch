import React, { useState } from 'react';
import Modal from '@mui/material/Modal';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';

const PopupModal = (props) => {
    console.warn(props.open);
  const [open, setOpen] = useState(false);

  const handleClose = () => {
    setOpen(false);
  };

  const handleOpen = () => {
    setOpen(true);
  };

  const body = (
    <Box sx={{ p: 2, backgroundColor: 'white', borderRadius: '8px' }}>
      <Typography variant="h5" sx={{ mb: 2 }}>
        Popup Modal Title
      </Typography>
      <Typography variant="body1">
        This is the content of the popup modal.
      </Typography>
    </Box>
  );

  return (
    <>
      <Modal
        open={open}
        onClose={handleClose}
        aria-labelledby="popup-modal-title"
        aria-describedby="popup-modal-description"
      >
        <Box
          sx={{
            position: 'absolute',
            top: '50%',
            left: '50%',
            transform: 'translate(-50%, -50%)',
            width: 400,
            bgcolor: 'background.paper',
            boxShadow: 24,
            p: 4,
          }}
        >
          {body}
        </Box>
      </Modal>
    </>
  );
};

export default PopupModal;