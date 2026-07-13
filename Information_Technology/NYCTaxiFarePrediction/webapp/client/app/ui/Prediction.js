import React from 'react';

const Prediction = ({ fare, duration }) => {
  return (
    <div className='mx-auto mt-5 text-center'>
      <h2 className='mb-4 text-2xl font-semibold text-yellow-500'>
        Prediction Result
      </h2>
      <div className='flex justify-center '>
        <div className='mb-3 mx-3'>
          <h3 className='block text-sm font-bold text-gray-700'>Fare:</h3>
          <p className='text-lg font-medium'>$us {fare}</p>
        </div>

        <div className='mb-3 mx-3'>
          <h3 className='block text-sm font-bold text-gray-700'>Duration:</h3>
          <p className='text-lg font-medium'>{duration} minutes</p>
        </div>
      </div>
    </div>
  );
};

export default Prediction;
