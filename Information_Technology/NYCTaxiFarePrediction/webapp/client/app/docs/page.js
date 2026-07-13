import Image from 'next/image';
import React from 'react';

const Docs = () => {
  return (
    <div className='docs-container p-8'>
      <h1 className='text-3xl font-bold mb-6'>
        NYC Taxi Fare and Trip Duration Prediction
      </h1>
      <Image
        src='/taxi.gif'
        alt='Project Workflow'
        width={500}
        height={500}
        // className='w-full mb-8'
      />
      <section className='project-info'>
        <h2 className='text-2xl font-bold mb-4'>Business Goal</h2>
        <p className='mb-4'>
          This project aims to leverage the vast amount of ride data in New York
          City to predict taxi ride fares and durations. The focus is on
          utilizing data available at the beginning of a ride, including
          pickup/dropoff coordinates, trip distance, start time, passenger
          count, and rate code (standard or airport). Predicting these factors
          can assist passengers in making informed commuting decisions and help
          drivers choose more profitable rides.
        </p>

        <p className='mb-4'>
          The project involves building predictive models trained on a dataset
          of NYC taxi rides, split into training and testing sets. Evaluation
          will be based on the model&apos;s accuracy in predicting fares and
          durations. Additionally, the project can extend to analyze factors
          impacting rides, such as traffic, weather, and road closures,
          providing insights for operational optimization and customer
          satisfaction.
        </p>

        <p>
          Furthermore, the project explores the potential to predict taxi
          demand, assisting dispatchers in decision-making for profit margin
          improvement. In summary, it offers an opportunity to apply machine
          learning to real-world data, gaining valuable insights into NYC&apos;s
          transportation industry.
        </p>
      </section>

      <section className='data-info mt-8'>
        <h2 className='text-2xl font-bold mb-4'>About the data</h2>
        <p className='mb-4'>
          The dataset can be accessed from the Official NYC web site. For this
          particular project, we advise you to use the 2022 TLC Trip Record Data
          given is the most complete and up-to-date dataset on the site at the
          moment.
        </p>

        <p className='mb-4'>
          We are going to use only the data corresponding to &quot;Yellow Taxi
          Trip Records&quot;.
        </p>

        <p>
          Because of the dataset size, it was split into separate files, one for
          each month of the year. You can start doing experiments using only one
          month of data. We advise you to use Yellow Taxi Trip Records (PARQUET)
          - May 2022 as a start.
        </p>
      </section>

      <section className='workflow-info mt-8'>
        <h2 className='text-2xl font-bold mb-4'>Project Workflow</h2>
        <Image
          src='/workflow.jpg'
          alt='Project Workflow Screenshot'
          width={800}
          height={500}
          // className='w-full mb-8'
        />
      </section>
    </div>
  );
};

export default Docs;
